from .utils.apply_blur import apply_blur
from .utils.apply_padding import apply_padding
from .utils.tensor_to_image import tensor_to_image
from .utils.image_to_tensor import image_to_tensor
from .utils.resize_image import resize_image

class ImagePadding:

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "image": ("IMAGE",),
                "padding": ("INT", {"default": 0, "min": 0, "max": 8192, "step": 1}),
                "blur": ("FLOAT", {"default": 0, "min": 0, "max": 50, "step": 0.1}),
                "color": (["black", "white","transparent"],)
            }
        }
    CATEGORY = "TrollSuite/image"
    RETURN_TYPES = ("IMAGE",)
    RETURN_NAMES = ("image",)
    FUNCTION = "ImagePadding"


    def ImagePadding(self, image, padding, blur, color):
        image = tensor_to_image(image)
        image = apply_padding(image, padding, color)
        image = apply_blur(image, blur)
        image = image_to_tensor(image)
        return (image,)
