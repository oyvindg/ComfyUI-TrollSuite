from PIL import Image, ImageOps
def apply_padding(image: Image, padding: float, fill: str)->Image:
    if padding is 0:
        return image
    if fill == "transparent":
        alpha = image.convert("RGBA")  # Ensure image has an alpha channel
        return ImageOps.expand(alpha, border=padding, fill=(0,0,0,0))  # Fill border with transparency
    else:
        return ImageOps.expand(image, border=padding, fill=fill)