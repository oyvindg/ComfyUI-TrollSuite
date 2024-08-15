import torch 
from PIL import Image

from .mask_to_image_tensor import mask_to_image_tensor
from .tensor_to_image import tensor_to_image

def mask_to_image(mask:torch.Tensor)->Image:
    return tensor_to_image(mask_to_image_tensor(mask))