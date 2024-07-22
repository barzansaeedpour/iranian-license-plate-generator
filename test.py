from PIL import Image

# Load the background image
background = Image.open("templates/taxi.png")

# Load the image with a transparent background
overlay = Image.open("chars/4.png")

# Create a new image with RGBA mode
new_image = Image.new("RGBA", background.size)

# Paste the overlay image onto the new image at the desired position
position = (100, 30)  # Specify the coordinates (x, y)
new_image.paste(overlay, position, overlay)

# Paste the new image onto the background image
# final_image = Image.alpha_composite(background.convert("RGBA"), new_image)

# Save the final image with the overlaid image
new_image.save("output_image.png")