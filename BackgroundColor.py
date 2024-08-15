from PIL import Image

from .utils.image_to_tensor import image_to_tensor
from .utils.tensor_to_image import tensor_to_image

class BackgroundColor:

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
               "image": ("IMAGE",),
               "mask": ("MASK",),
               "color": (["black", "white"],)
            }
        }
    CATEGORY = "TrollSuite/image"
    RETURN_TYPES = ("IMAGE","MASK",)
    RETURN_NAMES = ("image","mask",)
    FUNCTION = "BackgroundColor"


    def BackgroundColor(self, image, mask, color):
        image = tensor_to_image(image)
        image = Image.alpha_composite(Image.new("RGBA", image.size, color=color).convert("RGBA"), image.convert("RGBA"))
        image = image_to_tensor(image)
        return (image, mask,)
