from PIL import Image, ImageOps
def image_composite(image: Image, mask: Image, color: str = "black") -> Image:
    mask = mask.convert("L").resize(image.size)
    
    if color == "transparent":
        return ImageOps.invert(image).putalpha(mask)
    
    background_image = Image.new("RGB", image.size, color=color)
    return Image.composite(background_image, image, mask)