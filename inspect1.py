from PIL import Image

# Load the image
image_path = 'pallet.png'  # Replace with your image file path
image = Image.open(image_path)

# Specify the (x, y) coordinate of the pixel you want to inspect
x, y = 154, 132  # Replace with the exact coordinates

# Get the color at the specified pixel
color = image.getpixel((x, y))
print(f"The color at ({x}, {y}) is: {color}")
