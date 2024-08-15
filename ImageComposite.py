from .utils.apply_blur import apply_blur
from .utils.apply_padding import apply_padding
from .utils.tensor_to_image import tensor_to_image
from .utils.image_to_tensor import image_to_tensor
from .utils.image_to_mask import image_to_mask
from .utils.image_composite import image_composite

class ImageComposite:

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
               "image": ("IMAGE",),
               "mask": ("MASK",),
               "color": (["black", "white","transparent"],)
            }
        }
    CATEGORY = "TrollSuite/image"
    RETURN_TYPES = ("IMAGE","MASK",)
    RETURN_NAMES = ("image","mask",)
    FUNCTION = "ImageComposite"


    def ImageComposite(self, image, mask, color):
        image = image_composite(tensor_to_image(image), tensor_to_image(mask), color)
        image = image_to_tensor(image)
        return (image, mask,)
