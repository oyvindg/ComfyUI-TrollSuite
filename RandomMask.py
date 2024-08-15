
from PIL import Image
from torch import Tensor

from .utils.image_to_rgba import image_to_rgba
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
                "padding": ("INT", {"default": 0, "min": 0, "max": 512, "step": 1}),
                "blur": ("FLOAT", {"default": 0, "min": 0, "max": 50, "step": 0.1}),
                "noise": ("FLOAT", {"default": 0, "min": 0.0, "max": 1.0, "step": 0.1}),
                "background": (["black", "white"],)
            }
        }

    CATEGORY = "TrollSuite/mask"
    RETURN_TYPES = ("IMAGE", "MASK",)
    RETURN_NAMES = ("image", "mask",)
    FUNCTION = "RandomMask"

    def RandomMask(self, image: Tensor, padding: float, blur: float,noise: int, background: str) -> tuple[Tensor]:
        image:Image = tensor_to_image(image)
        
        mask_image:Image = create_random_mask(image.size, noise, background_color=background)
        mask_image = apply_padding(mask_image, padding, "black")
        mask_image = apply_blur(mask_image, blur)
        
        image = image_to_rgba(image, mask_image)
        #image = Image.new("RGB", mask_image.size, "black").paste(image, (0,0), mask=mask_image)
        image = image_to_tensor(image)
        
        mask_image = image_to_tensor(mask_image)
        mask = image_to_mask(mask_image)
        
        return (image, mask,)
    @classmethod
    def IS_CHANGED(self):
        return float("NaN")      
