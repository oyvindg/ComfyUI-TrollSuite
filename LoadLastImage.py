import os
import numpy as np
from PIL import Image, ImageOps
from torch import Tensor
from typing import Tuple
from .utils.image_to_tensor import image_to_tensor

class LoadLastImage:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "initial_image": ("IMAGE",),
                "save_initial_image": ("BOOLEAN", {"default": True}),
                "directory_path": ("STRING", {"multiline": False}),
                "sort": (["created", "modified"],)
            }
        }

    CATEGORY = "TrollSuite/image"
    RETURN_TYPES = ("IMAGE",)
    RETURN_NAMES = ("image",)
    FUNCTION = "LoadLastImage"

    def LoadLastImage(self, initial_image: Tensor, save_initial_image: bool, directory_path: str, sort: str) -> Tuple[Tensor]:
        image = initial_image
        if os.path.isabs(directory_path): 
            directory_path = os.path.abspath(directory_path)
        else:
            directory_path = os.path.join("./output", os.path.relpath(directory_path))
        
        # create directory 
        self.mkdirs(directory_path)

        # store initial image if dir is empty
        if save_initial_image and self.is_directory_empty(directory_path):
            for index, image in enumerate(image):
                i = 255. * image.cpu().numpy()
                img = Image.fromarray(np.clip(i, 0, 255).astype(np.uint8))
                img.save(os.path.join(directory_path, f"{index:05}_.png"), pnginfo=None, compress_level=0)

        filepath = self.get_last_filepath(directory_path, sort)
        if filepath:
            image = self.convert_to_tensor(filepath)
        return (image,)
     
    def get_last_filepath(self, directory_path:str, sort: str) -> str:
        """
        Get the latest image file in the given directory
        """
        # Resolve relative directories and remove trailing slashes
        directory_path = os.path.abspath(directory_path)

        # get filepaths of all files and dirs in the given dir
        valid_files = [os.path.join(directory_path, filename) 
               for filename in os.listdir(directory_path) 
               if os.path.isfile(os.path.join(directory_path, filename))]

        if not valid_files:
            return None

        if sort == "modified":
            key = os.path.getmtime
        else:
            key = os.path.getctime

        return max(valid_files, key=key) 
    
    def mkdirs(self, directory_path: str):
        """
        Creates the specified directory if it does not exist.
        """
        if not os.path.exists(directory_path):
            try:
                os.makedirs(directory_path)
            except OSError:
                print ("Creation of the directory %s failed" % directory_path)
    
    def is_directory_empty(self, directory_path:str):
       return not bool(os.listdir(directory_path))
    
    def convert_to_tensor(self, image_path: str) -> Tensor:
        i = Image.open(image_path)
        i = ImageOps.exif_transpose(i)
        image = i.convert("RGB")
        return image_to_tensor(image)
    
    @classmethod
    def IS_CHANGED(self):
        return float("NaN")      
