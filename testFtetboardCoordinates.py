from PIL import Image, ImageDraw, ImageFont
from fretboard_coordinates import fretboard_coordinates
from fretboard_notes import fretboard_notes

# Load the image
image_path = 'FRET3.png'  # Replace with the path to your image
image = Image.open(image_path)
draw = ImageDraw.Draw(image)

# Load a font with the desired size
font_path = "Open_Sans/static/OpenSans-Bold.ttf"  # Replace with the path to your .ttf font file
font_size = 50  # Set the font size
font = ImageFont.truetype(font_path, font_size)

# Define the radius for the circles
radius = 50

# Draw circles and notes at each coordinate
for key, (x, y) in fretboard_coordinates.items():
    note, octave, color = fretboard_notes.get(key, ("", "", "black"))  # Default to black if no color found
    
    # Handle the empty fill for certain colors (e.g., "gray" as None for transparency)
    fill_color = None if color == "gray" else color
    
    # Draw the circle with the specified color
    left_up_point = (x - radius, y - radius)
    right_down_point = (x + radius, y + radius)
    draw.ellipse([left_up_point, right_down_point], fill=fill_color, outline=color)

    # Get text bounding box for centering
    bbox = draw.textbbox((0, 0), note, font=font)
    text_width, text_height = bbox[2] - bbox[0], bbox[3] - bbox[1]
    
    # Calculate centered text position inside the circle
    #text_position = (x - text_width / 2, y - text_height / 2)
    text_position = (x - text_width / 2, y - text_height / 2 - font_size * 0.3 )
    
    # Draw the text at the centered position
    draw.text(text_position, note, fill="black", font=font)

# Save the updated image
output_path = 'fretboard_with_circles.png'  # Replace with your desired output path
image.save(output_path)
print(f"Image saved to {output_path}")
