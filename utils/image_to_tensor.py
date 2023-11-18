import torch 
from PIL import Image, ImageOps
import numpy as np

def image_to_tensor(image: Image) -> torch.Tensor:
        image = np.array(image).astype(np.float32) / 255.0
        return torch.from_numpy(image)[None,]