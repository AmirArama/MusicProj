from fretboard_notes import fretboard_notes

def filter_by_note(fretboard_notes, target_note):
    # Create a sub-dictionary for the target note
    filtered_notes = {
        key: value for key, value in fretboard_notes.items() if value[0] == target_note
    }
    return filtered_notes


# Example subset of notes after filtering
filtered_notes = {
    ("string_1", "fret_0"): ("E", 4, (178, 139, 90, 255)),
    ("string_1", "fret_5"): ("A", 4, (216, 158, 15, 255)),
    # Add more filtered notes as needed
}

# Append coordinates to the filtered notes
def append_coordinates(filtered_notes, fretboard_coordinates):
    updated_notes = {}
    for key, value in filtered_notes.items():
        # Find matching coordinates based on the same string and fret
        if key in fretboard_coordinates:
            coordinates = fretboard_coordinates[key]
            # Append the coordinates to the note's data
            updated_notes[key] = value + (coordinates,)
        else:
            updated_notes[key] = value  # If no coordinates found, keep as is
    return updated_notes

'''
# Usage
updated_notes_with_coordinates = append_coordinates(filtered_notes, fretboard_coordinates)

# Display the result
for key, value in updated_notes_with_coordinates.items():
    print(f"{key}: {value}")

# Example usage:
target_note = "A"
filtered_fretboard_notes = filter_by_note(fretboard_notes, target_note)

print(filtered_fretboard_notes)
'''