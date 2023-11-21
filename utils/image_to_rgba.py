from torchvision import transforms
from PIL import Image

def image_to_rgba(image: Image, gray_image: Image)->Image:
    
    # Resize the grayscale image to match the size of the color image
    resize_transform = transforms.Resize(image.size)
    gray_image = resize_transform(gray_image)
    if image.size != gray_image.size:
        gray_image = gray_image.resize(image.size)
    
    # Make sure image is RGBA format
    if image.mode != "RGBA":
        image = image.convert("RGBA")

    # Make sure gray_image is in mode 'L' (grayscale)
    if gray_image.mode != 'L':
        gray_image = gray_image.convert('L')

    # Copy the resized grayscale image into the alpha channel of the RGBA image
    image.putalpha(gray_image)

    return image
    