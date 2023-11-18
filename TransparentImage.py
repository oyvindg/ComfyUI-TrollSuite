from .utils.image_to_tensor import image_to_tensor
from .utils.image_to_rgba import image_to_rgba
from .utils.mask_to_image_tensor import mask_to_image_tensor
from .utils.tensor_to_image import tensor_to_image

class TransparentImage:

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "image": ("IMAGE",),
                "mask": ("MASK",)
            }
        }
    CATEGORY = "TrollSuite/image"
    RETURN_TYPES = ("IMAGE","MASK",)
    RETURN_NAMES = ("image","mask",)
    FUNCTION = "TransparentImage"

    def TransparentImage(self, image, mask):
        original_mask = mask
        image = tensor_to_image(image)
        mask = mask_to_image_tensor(mask)
        mask = tensor_to_image(mask)
        image = image_to_rgba(image, mask)
        image = image_to_tensor(image)
        return (image, original_mask,)