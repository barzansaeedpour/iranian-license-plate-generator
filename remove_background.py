
from PIL import Image


def remove_background(image,char_color):
    # Load the image
    # image = Image.open('chars/4.png')

    # Create a copy of the image with an alpha channel
    image = image.convert("RGBA")
    data = image.getdata()

    # Define the threshold for transparency
    threshold = 50
    new_data = []
    for item in data:
        if item[0] > threshold and item[1] > threshold and item[2] > threshold:
            new_data.append((255, 255, 255, 0))
        else:
            if char_color == 'black':
                new_data.append((0, 0, 0, 255))
            else:
                new_data.append((255, 255, 255, 255))
            # new_data.append(item)

    # Update the image data
    image.putdata(new_data)

    # Save the image with transparent background
    # image.save("EIN_T.png")
    return image

# def remove_background2():
#     import cv2
#     import numpy as np

#     # Load the image
#     image = cv2.imread(f"./chars/EIN.png")

#     # Convert the image to grayscale
#     gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#     # Apply thresholding to separate the object from the background
#     _, binary = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)

#     # Invert the binary image
#     binary = cv2.bitwise_not(binary)

#     # Apply bitwise AND operation to extract the object
#     result = cv2.bitwise_and(image, image, mask=binary)

#     # Save the result
#     cv2.imwrite(f"./chars/EIN_T.png", result)
#     image = cv2.imread(f"./chars/EIN_T.png")
#     gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#     cv2.imwrite(f"./chars/EIN_T.png", gray)
#     image = Image.open(f"./chars/EIN_T.png")
#     image = image.convert("RGBA")
#     data = image.getdata()
#     threshold = 50
#     new_data = []
#     for item in data:
#         if item[0] > threshold and item[1] > threshold and item[2] > threshold:
#             new_data.append((0, 0, 0, 255))
#         else:
#             new_data.append((255, 255, 255, 255))
#     # Update the image data
#     image.putdata(new_data)
#     # Save the image with transparent background
#     image.save(f"./chars/EIN_T.png")
# remove_background2()