from PIL import Image
def resize_image(image:Image, size: [int, int]): 
    image.thumbnail(size)
    return image