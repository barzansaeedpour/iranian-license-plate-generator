
from PIL import Image

# Load the image
image = Image.open('chars/4.jpg')

# Create a copy of the image with an alpha channel
image = image.convert("RGBA")
data = image.getdata()

# Define the threshold for transparency
threshold = 100
new_data = []
for item in data:
    if item[0] > threshold and item[1] > threshold and item[2] > threshold:
        new_data.append((255, 255, 255, 255))
    else:
        new_data.append(item)

# Update the image data
image.putdata(new_data)

# Save the image with transparent background
image.save("4.png")