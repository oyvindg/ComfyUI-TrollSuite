from .BinaryImageMask import BinaryImageMask
from .ImagePadding import ImagePadding
from .LoadLastImage import LoadLastImage
from .RandomMask import RandomMask
from .TransparentImage import TransparentImage

NODE_CLASS_MAPPINGS = {
    "BinaryImageMask": BinaryImageMask,
    "ImagePadding": ImagePadding,
    "LoadLastImage": LoadLastImage,
    "RandomMask": RandomMask,
    "TransparentImage": TransparentImage
}
__all__ = ["NODE_CLASS_MAPPINGS"]