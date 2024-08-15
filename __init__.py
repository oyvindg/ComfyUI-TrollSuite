from .BinaryImageMask import BinaryImageMask
from .BackgroundColor import BackgroundColor
from .ImageComposite import ImageComposite
from .ImagePadding import ImagePadding
from .LoadLastImage import LoadLastImage
from .RandomMask import RandomMask
from .TransparentImage import TransparentImage

NODE_CLASS_MAPPINGS = {
    "BinaryImageMask": BinaryImageMask,
    "ImagePadding": ImagePadding,
    "LoadLastImage": LoadLastImage,
    "ImageComposite": ImageComposite,
    "BackgroundColor": BackgroundColor,
    "RandomMask": RandomMask,
    "TransparentImage": TransparentImage
}
__all__ = ["NODE_CLASS_MAPPINGS"]