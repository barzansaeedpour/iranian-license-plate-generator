from PIL import Image
from remove_background import remove_background
# from remove_background import remove_background_HE
import os
import random
import json

os.makedirs('./output/',exist_ok=True)


with open('config.json', 'r') as file:
    data = json.load(file)
    
numbers = data['numbers']
mini_numbers = data['mini_numbers']
chars = data['chars']

for i in range(2):
    # Open the background image

    # Make a random choice from the list
    random_1 = random.choice(numbers)
    random_2 = random.choice(numbers)

    random_char = random.choice(chars)

    random_3 = random.choice(numbers)
    random_4 = random.choice(numbers)
    random_5 = random.choice(numbers)

    mini_random_1 = random.choice(mini_numbers)
    while mini_random_1["ch"]=='0':
        mini_random_1 = random.choice(mini_numbers)
    mini_random_2 = random.choice(mini_numbers)

    plate_text =  random_1['ch'] + random_2['ch']+ '-' +random_char['ch']+ '-' + random_3['ch'] + random_4['ch'] + random_5['ch']+ '-' + mini_random_1['ch'] + mini_random_2['ch']

    char_color = 'black'
    
    if random_char['ch']=='T' or random_char['ch'] == 'EIN':
        background = Image.open("templates/taxi.png")
    elif random_char['ch']=='P':
        background = Image.open("templates/police.png")
        char_color = 'white'
    else:
        background = Image.open("templates/savari.png")
    new_image = Image.new("RGBA", background.size)
    
    # if random_char['ch']=='HE':
    #     overlaych = remove_background_HE(Image.open(f"./chars/{random_char['ch']}.png"))
    #     # overlaych = remove_background(Image.open(f"./chars/{random_char['ch']}.png"))
    # else:     
       
    overlaych = remove_background(Image.open(f"./chars/{random_char['ch']}.png"),char_color = char_color)
    # overlaych.save(f"./resized_chars/{random_char['ch']}.png")

    
    overlay1 = remove_background(Image.open(f"./chars/{random_1['ch']}.png"),char_color = char_color)
    overlay1 = overlay1.resize(random_1['size'])
    # overlay1.save(f"./resized_chars/{random_1['ch']}.png") 
    new_image.paste(overlay1, [100, random_1['position'][1]])
    final_image = Image.alpha_composite(background.convert("RGBA"), new_image)

    overlay2 = remove_background(Image.open(f"./chars/{random_2['ch']}.png"),char_color = char_color)
    overlay2 = overlay2.resize(random_2['size'])
    # overlay2.save(f"./resized_chars/{random_2['ch']}.png") 
    new_image.paste(overlay2, [180, random_2['position'][1]])
    final_image = Image.alpha_composite(final_image.convert("RGBA"), new_image)


    position = random_char['position']  # Specify the coordinates (x, y)
    overlaych = overlaych.resize(random_char['size'])
    # overlaych.save(f"./resized_chars/{random_char['ch']}.png") 
    new_image.paste(overlaych, position)
    final_image = Image.alpha_composite(final_image.convert("RGBA"), new_image)

    overlay3 = remove_background(Image.open(f"./chars/{random_3['ch']}.png"), char_color = char_color)
    overlay3 = overlay3.resize(random_3['size'])
    # overlay3.save(f"./resized_chars/{random_3['ch']}.png")
    new_image.paste(overlay3, [390, random_3['position'][1]])
    final_image = Image.alpha_composite(final_image.convert("RGBA"), new_image)
 
    # background.paste(overlay3, [390, random_3['position'][1]])

    overlay4 = remove_background(Image.open(f"./chars/{random_4['ch']}.png"), char_color = char_color)
    overlay4 = overlay4.resize(random_4['size'])
    # overlay4.save(f"./resized_chars/{random_4['ch']}.png") 
    new_image.paste(overlay4, [470, random_4['position'][1]])
    final_image = Image.alpha_composite(final_image.convert("RGBA"), new_image)
    # background.paste(overlay4, [470, random_4['position'][1]])

    overlay5 = remove_background(Image.open(f"./chars/{random_5['ch']}.png"), char_color = char_color)
    overlay5 = overlay5.resize(random_5['size'])
    # overlay5.save(f"./resized_chars/{random_5['ch']}.png") 
    new_image.paste(overlay5, [550, random_5['position'][1]])
    final_image = Image.alpha_composite(final_image.convert("RGBA"), new_image)
    # background.paste(overlay5, [550, random_5['position'][1]])

    overlay6 = remove_background(Image.open(f"./chars/{mini_random_1['ch']}.png"), char_color = char_color)
    overlay6 = overlay6.resize(mini_random_1['size'])
    # overlay6.save(f"./resized_chars/{mini_random_1['ch']}.png")
    new_image.paste(overlay6, [655, mini_random_1['position'][1]])
    final_image = Image.alpha_composite(final_image.convert("RGBA"), new_image) 
    # background.paste(overlay6, [655, mini_random_1['position'][1]])

    overlay7 = remove_background(Image.open(f"./chars/{mini_random_2['ch']}.png"), char_color = char_color)
    overlay7 = overlay7.resize(mini_random_2['size'])
    # overlay7.save(f"./resized_chars/{mini_random_2['ch']}.png")
    new_image.paste(overlay7, [720, mini_random_2['position'][1]])
    final_image = Image.alpha_composite(final_image.convert("RGBA"), new_image) 
    # background.paste(overlay7, [720, mini_random_2['position'][1]])



    # Save the final image with the overlay
    # with open(f"output/output_image_{i}.txt",'w') as f:
    #     f.write(plate_text)
    final_image.save(f"output/{i}_{plate_text}.png")