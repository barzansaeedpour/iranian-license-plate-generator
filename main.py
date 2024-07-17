from PIL import Image, ImageDraw, ImageFont
import arabic_reshaper
from bidi.algorithm import get_display

def persian(text):
    return get_display(arabic_reshaper.reshape(text))
    # return text

import random
from offsets import letters
# x = letters.items()

num_img = 20

x = lambda t : str(random.randint(1,9)) 

for n in range(num_img):

    counter=0
    for k,v in letters.items():
        # print(k,v)
        # Open an image file
        template_path = './templates/savari.png'
        # font_path = './fonts/khorshid.ttf'
        font_path = './fonts/BZarBd.ttf'

        image = Image.open(template_path)

        # Initialize the drawing context
        draw = ImageDraw.Draw(image)

        plate_text=[x(0),x(0),k,x(0),x(0),x(0),x(0),x(0)]

        positions = [
            [80, 35],
            [150,35],
            v,
            [380,35],
            [460,35],
            [540,35],
            [640,35],
            [712,35],
            ]

        for i in range(len(plate_text)):
            # Define the text to be added
            # text = "1"
            text = plate_text[i]
            # Load a custom font
            if i==2:
                font = ImageFont.truetype(font_path, size=118)
            else:
                font = ImageFont.truetype(font_path, size=140)
            # Specify the position to add the text
            # Add text to the image
            draw.text(positions[i], persian(text), fill="black", font=font)
            
            
        # Save the modified image
        image.save(f"./output/output_{n}_{counter}.png")
        print("Text added successfully!")
        counter+=1