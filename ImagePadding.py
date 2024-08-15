from .utils.mask_to_image import mask_to_image
from .utils.apply_blur import apply_blur
from .utils.apply_padding import apply_padding
from .utils.tensor_to_image import tensor_to_image
from .utils.image_to_tensor import image_to_tensor
from .utils.image_to_mask import image_to_mask

class ImagePadding:

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "image": ("IMAGE",),
                "mask": ("MASK",),
                "padding": ("INT", {"default": 0, "min": 0, "max": 8192, "step": 1}),
                "blur": ("FLOAT", {"default": 0, "min": 0, "max": 50, "step": 0.1}),
                "color": (["black", "white","transparent"],)
            }
        }
    CATEGORY = "TrollSuite/image"
    RETURN_TYPES = ("IMAGE","MASK",)
    RETURN_NAMES = ("image","mask",)
    FUNCTION = "ImagePadding"


    def ImagePadding(self, image, mask, padding, blur, color):

        # image
        image = tensor_to_image(image)
        image = apply_padding(image, padding, color)
        image = apply_blur(image, blur)
        image = image_to_tensor(image)
        image = image[..., :3]

        # mask
        mask_image = mask_to_image(mask)
        mask_image = apply_padding(mask_image, padding, color)
        mask_image = apply_blur(mask_image, blur)
        mask = image_to_mask(image_to_tensor(mask_image))

        return (image,mask,)
