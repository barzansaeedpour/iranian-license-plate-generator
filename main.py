import argparse
import json
import os
import random
from typing import List

from PIL import Image

from utils import create_overlay, get_background, remove_background

# get input args for output directory and number of images
parser = argparse.ArgumentParser(description="Iranina license plate generator")
parser.add_argument('-o', '--output_dir', type=str, help='Path to the output directory', default='./output/')
parser.add_argument('-n', '--num_samples', type=int, help='Number of samples to process', default=100)

args = parser.parse_args()
output_dir = args.output_dir
num_samples = args.num_samples

# Create the output directory if it doesn't exist
if not os.path.exists(output_dir):
	os.makedirs(output_dir)

# Load JSON data from a file
with open('number_char_config.json', 'r') as file:
	data = json.load(file)

chars = data['chars']
numbers = data['numbers']
mini_numbers = data['mini_numbers']

def choose_random_items(items: List, count: int) -> list:
	# Remove the first item if it is 0
	if items == mini_numbers:
		non_zero_mini_numbers = [item for item in mini_numbers if item["ch"] != '0']
		first_mini_number = random.choice(non_zero_mini_numbers)
		return [first_mini_number] + random.sample(items, count-1)
	
	return random.sample(items, count)

def main() -> None:

	for i in range(num_samples):
		# generate random license plate items containing numbers, characters, and mini numbers
		random_char = choose_random_items(chars, count=1)[0]
		random_numbers = choose_random_items(numbers, count=6)
		mini_random_numbers = choose_random_items(mini_numbers, count=2)
        
		# create license plate items
		license_plate_items = [
			{"ch": random_numbers[0]['ch'], "size": random_numbers[0]['size'], "position": [100, random_numbers[0]['position'][1]]},
			{"ch": random_numbers[1]['ch'], "size": random_numbers[1]['size'], "position": [180, random_numbers[1]['position'][1]]},
			{"ch": random_char['ch'], "size": random_char['size'], "position": random_char['position']},
			{"ch": random_numbers[2]['ch'], "size": random_numbers[2]['size'], "position": [390, random_numbers[2]['position'][1]]},
			{"ch": random_numbers[3]['ch'], "size": random_numbers[3]['size'], "position": [470, random_numbers[3]['position'][1]]},
			{"ch": random_numbers[4]['ch'], "size": random_numbers[4]['size'], "position": [550, random_numbers[4]['position'][1]]},
			{"ch": mini_random_numbers[0]['ch'], "size": mini_random_numbers[0]['size'], "position": [655, mini_random_numbers[0]['position'][1]]},
			{"ch": mini_random_numbers[1]['ch'], "size": mini_random_numbers[1]['size'], "position": [720, mini_random_numbers[1]['position'][1]]}
		]

		background, char_color = get_background(random_char)
		new_image = Image.new("RGBA", background.size)

		# build license plate image
		for item in license_plate_items:
			image_path = f"./chars/{item['ch']}.png"
			new_image = create_overlay(image_path, char_color = char_color, size = item['size'], position = item['position'], new_image = new_image)
			final_image = Image.alpha_composite(background.convert("RGBA"), new_image)

		# Save the final image
		final_image.save(f"{output_dir}/output_image_{i}.png")

if __name__ == "__main__":
	main()