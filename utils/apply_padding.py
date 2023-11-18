from PIL import Image, ImageOps
def apply_padding(image: Image, padding: float, fill: str)->Image:
    if padding is 0:
        return image
    return ImageOps.expand(image, border=padding, fill=fill)