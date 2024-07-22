from PIL import Image
from remove_background import remove_background
# from remove_background import remove_background_HE

import random

# List of items to choose from
numbers = [
        #   {"ch":'1',
        #    "position":[100, 30],
        #    "size":[40, 115],
        #    },
        #   {"ch":'2',
        #    "position":[100, 30],
        #    "size":[60, 115],
        #    },
        #   {"ch":'3',
        #    "position":[100, 30],
        #    "size":[60, 115],
        #    },
        #   {"ch":'4',
        #    "position":[100, 30],
        #    "size":[60, 115],
        #    },
          {"ch":'5',
           "position":[100, 30],
           "size":[60, 115],
           },
        #   {"ch":'6',
        #    "position":[100, 30],
        #    "size":[60, 115],
        #    },
        #   {"ch":'7',
        #    "position":[100, 30],
        #    "size":[60, 115],
        #    },
        #   {"ch":'8',
        #    "position":[100, 30],
        #    "size":[60, 115],
        #    },
        #   {"ch":'9',
        #    "position":[100, 30],
        #    "size":[60, 115],
        #    },
        ]
mini_numbers = [
          {"ch":'0',
           "position":[100, 90],
           "size":(40, 40),
           },
          {"ch":'1',
           "position":[100, 50],
           "size":(40, 100),
           },
          {"ch":'2',
           "position":[100, 50],
           "size":(57, 100),
           },
          {"ch":'3',
           "position":[100, 50],
           "size":(57, 100),
           },
          {"ch":'4',
           "position":[100, 50],
           "size":(57, 100),
           },
          {"ch":'5',
           "position":[100, 50],
           "size":(57, 100),
           },
          {"ch":'6',
           "position":[100, 50],
           "size":(57, 100),
           },
          {"ch":'7',
           "position":[100, 50],
           "size":(57, 100),
           },
          {"ch":'8',
           "position":[100, 50],
           "size":(57, 100),
           },
          {"ch":'9',
           "position":[100, 50],
           "size":(57, 100),
           },
        ]

chars = [ 
        #  {"ch":'B',
        #    "position":(260, 50),
        #    "size":(110, 90),
        #    },
        #  {"ch":'N',
        #    "position":(265, 35),
        #    "size":(100, 100),
        #    },
        #  {"ch":'T',
        #    "position":(252, 30),
        #    "size":(120, 110),
        #    },
        #  {"ch":'H',
        #    "position":(275, 50),
        #    "size":(80, 80),
        #    },
        #  {"ch":'D',
        #    "position":(270, 40),
        #    "size":(90, 90),
        #    },
        #  {"ch":'Q',
        #    "position":(265, 40),
        #    "size":(100, 100),
        #    },
        #  {"ch":'J',
        #    "position":(265, 40),
        #    "size":(100, 100),
        #    },
        #  {"ch":'HE',
        #    "position":(265, 40),
        #    "size":(100, 100),
        #    },
        #  {"ch":'SIN',
        #    "position":(260, 55),
        #    "size":(110, 80),
        #    },
        #  {"ch":'SAD',
        #    "position":(260, 55),
        #    "size":(110, 80),
        #    },
        #  {"ch":'TA',
        #    "position":(270, 30),
        #    "size":(90, 110),
        #    },
        #  {"ch":'V',
        #    "position":(280, 40),
        #    "size":(70, 100),
        #    },
        #  {"ch":'M',
        #    "position":(280, 40),
        #    "size":(70, 100),
        #    },
        #  {"ch":'Y',
        #    "position":(270, 40),
        #    "size":(90, 100),
        #    },
        #  {"ch":'L',
        #    "position":(275, 35),
        #    "size":(70, 110),
        #    },
         ]


for i in range(1):
    # Open the background image
    background = Image.open("templates/savari2.png")

    # Make a random choice from the list
    random_1 = random.choice(numbers)
    random_2 = random.choice(numbers)

    random_char = random.choice(chars)

    random_3 = random.choice(numbers)
    random_4 = random.choice(numbers)
    random_5 = random.choice(numbers)
    random_6 = random.choice(numbers)

    mini_random_1 = random.choice(mini_numbers)
    while mini_random_1["ch"]=='0':
        mini_random_1 = random.choice(mini_numbers)
    mini_random_2 = random.choice(mini_numbers)



    # if random_char['ch']=='HE':
    #     overlaych = remove_background_HE(Image.open(f"./chars/{random_char['ch']}.png"))
    #     # overlaych = remove_background(Image.open(f"./chars/{random_char['ch']}.png"))
    # else:        
    overlaych = remove_background(Image.open(f"./chars/{random_char['ch']}.png"))

    overlay1 = remove_background(Image.open(f"./chars/{random_1['ch']}.png"))
    overlay1 = overlay1.resize(random_1['size']) 
    background.paste(overlay1, [100, random_1['position'][1]])

    overlay2 = remove_background(Image.open(f"./chars/{random_2['ch']}.png"))
    overlay2 = overlay2.resize(random_2['size']) 
    background.paste(overlay2, [180, random_2['position'][1]])


    position = random_char['position']  # Specify the coordinates (x, y)
    overlaych = overlaych.resize(random_char['size']) 
    background.paste(overlaych, position)

    overlay3 = remove_background(Image.open(f"./chars/{random_3['ch']}.png"))
    overlay3 = overlay3.resize(random_3['size']) 
    background.paste(overlay3, [390, random_3['position'][1]])

    overlay4 = remove_background(Image.open(f"./chars/{random_4['ch']}.png"))
    overlay4 = overlay4.resize(random_4['size']) 
    background.paste(overlay4, [470, random_4['position'][1]])

    overlay5 = remove_background(Image.open(f"./chars/{random_5['ch']}.png"))
    overlay5 = overlay5.resize(random_5['size']) 
    background.paste(overlay5, [550, random_5['position'][1]])

    overlay6 = remove_background(Image.open(f"./chars/{mini_random_1['ch']}.png"))
    overlay6 = overlay6.resize(mini_random_1['size']) 
    background.paste(overlay6, [655, mini_random_1['position'][1]])

    overlay7 = remove_background(Image.open(f"./chars/{mini_random_2['ch']}.png"))
    overlay7 = overlay7.resize(mini_random_2['size']) 
    background.paste(overlay7, [720, mini_random_2['position'][1]])


    # Save the final image with the overlay
    background.save(f"output/output_image_{i}.png")