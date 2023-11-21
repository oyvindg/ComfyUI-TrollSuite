from torch import Tensor
from typing import Tuple

from .utils.scale_up import scale_up
from .utils.tensor_to_image import tensor_to_image
from .utils.image_to_tensor import image_to_tensor

class BinaryImageMask:
    @classmethod
    def INPUT_TYPES(s):
        return {"required":
                    {
                        "image": ("IMAGE",),
                        "threshold": ("FLOAT", {"default": 0.5, "min": 0.1, "max": 1.0, "step": 0.1}),
                        
                     }
                }

    CATEGORY = "TrollSuite/mask"
    RETURN_TYPES = ("IMAGE","MASK",)
    RETURN_NAMES = ("image","mask",)

    FUNCTION = "BinaryImageMask"

    def BinaryImageMask(self, image: Tensor, threshold: float) -> Tuple[Tensor, Tensor]:
        original_image = image
        image = tensor_to_image(image)
        image = image.convert("L")
        threshold = scale_up(threshold)
        image = image.point(lambda x: 255 if x > threshold else 0)
        image = image_to_tensor(image)
        mask = image[:,:,:]
        return (original_image,mask,)
    
    @classmethod
    def IS_CHANGED(self):
        return float("NaN")      
