from .BinaryImageMask import BinaryImageMask
from .ImagePadding import ImagePadding
from .LoadLastCreatedImage import LoadLastCreatedImage
from .RandomMask import RandomMask
from .TransparentImage import TransparentImage

NODE_CLASS_MAPPINGS = {
    "BinaryImageMask": BinaryImageMask,
    "ImagePadding": ImagePadding,
    "LoadLastCreatedImage": LoadLastCreatedImage,
    "RandomMask": RandomMask,
    "TransparentImage": TransparentImage
}
__all__ = ["NODE_CLASS_MAPPINGS"]