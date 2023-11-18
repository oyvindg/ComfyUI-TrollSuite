import torch
from PIL import Image
import numpy as np

def tensor_to_image(image: torch.Tensor):
    for index, image in enumerate(image):
        i = 255. * image.cpu().numpy()
        return Image.fromarray(np.clip(i, 0, 255).astype(np.uint8))