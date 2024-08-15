import numpy as np
from PIL import Image
from io import BytesIO
import matplotlib.pyplot as plt

def create_random_mask(size, noise, background_color="white"):

    foreground_color = "black"
    if background_color == "black":
        foreground_color = "white"

    # scale noise
    noise = int(noise * (100 - 20) + 20)

    # Define theta as the angle formed from 0 to 2*pi
    theta = np.linspace(0, 2.*np.pi, noise)
    
    # Define the radius with random noise
    r = 1 + 0.1 * np.random.rand((noise))
    
    # Adding this line will make sure that the circle closes 
    r = np.append(r, r[0])
    theta = np.append(theta, theta[0])
    
    # Calculate x and y coordinates
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    
    # Draw the figure with black background
    fig, ax = plt.subplots(figsize=(6, 6), facecolor=background_color)
    
    ax.plot(x, y, color=foreground_color, lw=2)  # Change the color of the wave to white
    ax.fill(x, y, foreground_color)  # fill the circle with white color
    ax.set_aspect('equal', adjustable='box') # This line ensures the circle is not an ellipse
    
    # Remove axes for a cleaner look
    ax.axis('off')
    
    plt.margins(0,0)
    plt.subplots_adjust(top = 1, bottom = 0, right = 1, left = 0, hspace = 0, wspace = 0)
    
    # create buffer
    buf = BytesIO()
    plt.savefig(buf, format="png", bbox_inches="tight")
    buf.seek(0)
    
    # create image
    image = Image.open(buf)
    image_size = min(size)
    image = image.resize((image_size, image_size))
    
    # create black background with original size
    background_image = Image.new("RGB", size, background_color)

    # find centered position
    lw, lh = background_image.size
    sw, sh = image.size
    position = ((lw - sw) // 2, (lh - sh) // 2)

    # paste the mask on background
    background_image.paste(image, position)

    return background_image
