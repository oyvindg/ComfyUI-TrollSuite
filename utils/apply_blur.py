from PIL import Image, ImageFilter

def apply_blur(image: Image, radius: float)->Image:
    if radius == 0:
        return image
    return image.filter(ImageFilter.GaussianBlur(radius=radius))
