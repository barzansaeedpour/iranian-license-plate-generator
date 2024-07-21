from PIL import Image
from remove_background import remove_background

# Open the background image
background = Image.open("templates/savari2.png")


import random

# List of items to choose from
numbers = [
          {"ch":'1',
           "position":[100, 30],
           "size":[40, 115],
           },
          {"ch":'2',
           "position":[100, 30],
           "size":[60, 115],
           },
          {"ch":'3',
           "position":[100, 30],
           "size":[60, 115],
           },
        ]
mini_numbers = []
chars = [ 
         {"ch":'T',
           "position":(240, 30),
           "size":(120, 110),
           },
         {"ch":'H',
           "position":(260, 50),
           "size":(80, 80),
           },
        #  'D', 'Q', 'HE', 'J', 'L', 'M', 'SAD', 'SIN', 'TA', 'V', 'Y'
         ]

# Make a random choice from the list
random_1 = random.choice(numbers)
random_2 = random.choice(numbers)
random_char = random.choice(chars)

print("Random choice:", random_char)


# Open the image to be overlaid
overlay0 = remove_background(Image.open("./chars/0.png"))
overlay2 = remove_background(Image.open("./chars/2.png"))
overlay5 = remove_background(Image.open("./chars/5.png"))
overlay6 = remove_background(Image.open("./chars/6.png"))
overlay7 = remove_background(Image.open("./chars/7.png"))
overlay9 = remove_background(Image.open("./chars/9.png"))
# overlaysin = remove_background(Image.open("./chars/SIN.png"))
overlaych = remove_background(Image.open(f"./chars/{random_char['ch']}.png"))
# Set the position where the overlay image will be placed

overlay1 = remove_background(Image.open(f"./chars/{random_1['ch']}.png"))
overlay1 = overlay1.resize(random_1['size']) 
background.paste(overlay1, [100, random_1['position'][1]])

overlay2 = remove_background(Image.open(f"./chars/{random_2['ch']}.png"))
overlay2 = overlay2.resize(random_2['size']) 
background.paste(overlay2, [170, random_2['position'][1]])

# position = (160, 30)  # Specify the coordinates (x, y)
# overlay5 = overlay5.resize((60, 115)) 
# background.paste(overlay5, position)

position = random_char['position']  # Specify the coordinates (x, y)
overlaych = overlaych.resize(random_char['size']) 
background.paste(overlaych, position)

position = (380, 30)  # Specify the coordinates (x, y)
overlay5 = overlay5.resize((60, 115)) 
background.paste(overlay5, position)

position = (460, 30)  # Specify the coordinates (x, y)
overlay7 = overlay7.resize((60, 115)) 
background.paste(overlay5, position)

position = (550, 30)  # Specify the coordinates (x, y)
overlay1 = overlay1.resize((40, 115)) 
background.paste(overlay5, position)

position = (662, 50)  # 4
overlay2 = overlay2.resize((63, 100)) # 4
# overlay1 = overlay1.resize((57, 100)) # 4
background.paste(overlay5, position)


position = (730, 90)  # Specify the coordinates (x, y)
overlay0 = overlay0.resize((40, 40)) 
background.paste(overlay5, position)


# Save the final image with the overlay
background.save("output_image.png")