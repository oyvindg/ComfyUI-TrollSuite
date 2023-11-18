from torch import Tensor
def image_to_mask(image:Tensor): 
    return image[:, :, :, 2]
    