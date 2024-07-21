from PIL import Image

# Open the background image
background = Image.open("templates/savari2.png")

# Open the image to be overlaid
overlay = Image.open("4.png")
# Set the position where the overlay image will be placed
position = (90, 40)  # Specify the coordinates (x, y)
overlay = overlay.resize((57, 100))

# Paste the overlay image on top of the background image
background.paste(overlay, position)

# Save the final image with the overlay
background.save("output_image.png")