from PIL import Image, ImageDraw, ImageFont
from fretboard_coordinates import fretboard_coordinates
from fretboard_notes2 import fretboard_notes
import os

# Create a directory to save individual note images
os.makedirs("notes", exist_ok=True)

# Load the original image
image_path = 'FRET3.png'  # Replace with the path to your image
original_image = Image.open(image_path)

# Define padding sizes
padding_top = 50
padding_left = 200

# Create a new image with transparent padding on top and left
new_width = original_image.width + padding_left
new_height = original_image.height + padding_top
new_image = Image.new("RGBA", (new_width, new_height), (255, 255, 255, 0))  # Fully transparent

# Paste the original image onto the new image at the offset (padding_left, padding_top)
new_image.paste(original_image, (padding_left, padding_top))

# Now draw on the new image with padding
draw = ImageDraw.Draw(new_image)

# Load a font with the desired size
font_path = "Open_Sans/static/OpenSans-Bold.ttf"  # Replace with the path to your .ttf font file
font_size = 50  # Set the font size
font = ImageFont.truetype(font_path, font_size)

# Define the radius for the circles
radius = 50

# Keep track of generated notes to avoid duplicates
generated_notes = {}

# Draw circles and notes at each coordinate
for key, (x, y) in fretboard_coordinates.items():
    # Adjust x and y coordinates to account for padding
    x += padding_left
    y += padding_top

    note, octave, color = fretboard_notes.get(key, ("", "", "black"))  # Default to black if no color found
    
    # Handle the empty fill for certain colors (e.g., "gray" as None for transparency)
    fill_color = 'white' if color == "gray" else color
    
    #fill_color=(178, 139, 90, 255)
    # Draw the circle with the specified color
    left_up_point = (x - radius, y - radius)
    right_down_point = (x + radius, y + radius)
    draw.ellipse([left_up_point, right_down_point], fill=fill_color, outline=color)

    # Get text bounding box for centering
    bbox = draw.textbbox((0, 0), note, font=font)
    text_width, text_height = bbox[2] - bbox[0], bbox[3] - bbox[1]
    
    # Calculate centered text position inside the circle with slight vertical adjustment
    text_position = (x - text_width / 2, y - text_height / 2 - font_size * 0.3)
    
    # Draw the text at the centered position
    fontcolor = "white"
    if fill_color=='white':
        fontcolor="black"
        
    draw.text(text_position, note, fill=fontcolor, font=font)

    # Generate individual PNG for each unique note
    if note not in generated_notes:
        note_image_size = (2 * radius, 2 * radius)
        note_image = Image.new("RGBA", note_image_size, (255, 255, 255, 0))  # Transparent background
        note_draw = ImageDraw.Draw(note_image)
        
        # Draw the circle
        note_draw.ellipse([(0, 0), (note_image_size[0] - 1, note_image_size[1] - 1)], fill=fill_color, outline=color)
        
        # Draw the note text centered in the small circle
        text_position_note = ((note_image_size[0] - text_width) / 2, (note_image_size[1] - text_height) / 2 - font_size * 0.3)
        # Draw the text at the centered position
        fontcolor = "white"
        if fill_color=='white':
            fontcolor="black"
        note_draw.text(text_position_note, note, fill=fontcolor, font=font)
        
        # Save the individual note image
        note_filename = f"notes/note_{note}.png"
        note_image.save(note_filename)
        generated_notes[note] = note_filename  # Mark this note as generated

# Save the updated image with padding
output_path = 'fretboard_with_padding.png'  # Replace with your desired output path
new_image.save(output_path)
print(f"Image saved to {output_path}")
print("Individual note images saved in the 'notes' directory.")
