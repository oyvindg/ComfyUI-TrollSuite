
import random
from PIL import Image, ImageDraw
from torch import Tensor
from .utils.apply_padding import apply_padding
from .utils.apply_blur import apply_blur
from .utils.tensor_to_image import tensor_to_image
from .utils.image_to_tensor import image_to_tensor
from .utils.image_to_mask import image_to_mask
from .utils.create_random_mask import create_random_mask

class RandomMask:
    @classmethod
    def INPUT_TYPES(s):
        return {"required": {
                "image": ("IMAGE",),
                "noise": ("FLOAT", {"default": 0, "min": 0.0, "max": 1.0, "step": 0.1}),
                "padding": ("INT", {"default": 0, "min": 0, "max": 512, "step": 1}),
                "blur": ("FLOAT", {"default": 0, "min": 0, "max": 50, "step": 0.1}),
            }
        }

    CATEGORY = "TrollSuite/mask"
    RETURN_TYPES = ("IMAGE", "MASK",)
    RETURN_NAMES = ("image", "mask",)
    FUNCTION = "RandomMask"

    def RandomMask(self, image: Tensor, noise: int, padding: float, blur: float) -> tuple[Tensor]:
        original_image = image
        image:Image = tensor_to_image(image)
        image:Image = create_random_mask(image.size, noise)
        image = apply_padding(image, padding, "black")
        image = apply_blur(image, blur)
        image = image_to_tensor(image)
        mask = image_to_mask(image)
        return (original_image, mask,)
    
    def draw_image_shape(self, size, facets) -> Image:
        width, height = size

        image = Image.new("RGB", size, "black")
        draw = ImageDraw.Draw(image)
        center = width // 2, height // 2
        radius = min(center[0] - 15, center[1] - 15) // 2

        for _ in range(facets):
            self.draw_ellipse(draw, center, radius, "white")
        return image
    
    # draw an ellipse at a random location around the center
    def draw_ellipse(self, draw:ImageDraw, center, radius:int, color):
        x_offset = random.randint(-radius, radius)
        y_offset = random.randint(-radius, radius)
        x0 = center[0] + x_offset - radius
        y0 = center[1] + y_offset - radius
        x1 = center[0] + x_offset + radius
        y1 = center[1] + y_offset + radius
        return draw.ellipse([x0, y0, x1, y1], fill=color)

    @classmethod
    def IS_CHANGED(self):
        return float("NaN")      
