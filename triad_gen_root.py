
'''
Expected Combinations:

We have 3 triad types (major, minor, diminished).
Each triad type has 12 root notes (C, C#, D, D#, E, F, F#, G, G#, A, A#, B).
Each triad can be played in 3 inversions (root position, 1st inversion, 2nd inversion).
Each triad can be played across 4 string sets (123, 234, 345, 456).
This gives a theoretical maximum of:

3x12x3x4 = 432 possible combinations
Some triad notes may only appear in positions that cannot be arranged on the specified strings.

138 posible combinations
'''

# Chromatic notes and interval definitions for each triad type
chromatic_notes = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
intervals = {
    "major": [0, 4, 7],       # Root, Major Third, Perfect Fifth
    "minor": [0, 3, 7],       # Root, Minor Third, Perfect Fifth
    "diminished": [0, 3, 6]   # Root, Minor Third, Diminished Fifth
}

# String sets for triads
string_sets = {
    "123": ["string_1", "string_2", "string_3"],
    "234": ["string_2", "string_3", "string_4"],
    "345": ["string_3", "string_4", "string_5"],
    "456": ["string_4", "string_5", "string_6"]
}

# Merging fretboard_notes with fretboard_coordinates to include all details
def merge_fretboard_data(fretboard_notes, fretboard_coordinates):
    merged_fretboard = {}
    for key, (note, octave, color) in fretboard_notes.items():
        if key in fretboard_coordinates:
            position = fretboard_coordinates[key]
            merged_fretboard[key] = (note, octave, position, color)
    return merged_fretboard

# Function to generate triad notes based on intervals
def generate_triad_notes(root_index, intervals):
    return [chromatic_notes[(root_index + interval) % 12] for interval in intervals]

# Function to find positions for each note in a given string set
def find_positions_for_triad_in_set(triad_notes, string_set, fretboard_notes):
    positions = []
    for string in string_set:
        found_note = False
        # Search for each note in the triad on the specified strings
        for (s, fret), values in fretboard_notes.items():
            if len(values) == 4:
                note, octave, position, color = values
            elif len(values) == 3:
                note, octave, position = values
                color = None  # Default color if not provided

            if s == string and note in triad_notes:
                positions.append((note, s, fret, octave, position, color))
                triad_notes = tuple(n for n in triad_notes if n != note)  # Remove matched note
                found_note = True
                break  # Move to the next string after finding the note

        if not found_note:
            # If a note in triad isn't found on the specified string set
            return None
    return tuple(positions) if len(positions) == 3 else None

# Generate all triads for each note in the chromatic scale with positions on the fretboard
def generate_all_triads(fretboard_notes):
    all_triads_positions = {}
    for triad_type, triad_intervals in intervals.items():
        for root_index, root_note in enumerate(chromatic_notes):
            root_position_notes = generate_triad_notes(root_index, triad_intervals)
            
            # Define inversions of the triad
            inversions = {
                "root_position": root_position_notes,
                "1st_inversion": [root_position_notes[1], root_position_notes[2], root_position_notes[0]],
                "2nd_inversion": [root_position_notes[2], root_position_notes[0], root_position_notes[1]]
            }

            # Loop through each inversion and string set to find fretboard positions
            for inversion_name, notes in inversions.items():
                for set_name, strings in string_sets.items():
                    positions = find_positions_for_triad_in_set(notes, strings, fretboard_notes)
                    if positions:
                        # Add to dictionary if a valid position was found
                        all_triads_positions[(triad_type, root_note, set_name, inversion_name)] = positions
    return all_triads_positions

# Import data
from fretboard_notes import fretboard_notes  # Note, octave, color
from fretboard_coordinates import fretboard_coordinates  # Coordinates for each string and fret

# Merge fretboard data
merged_fretboard_notes = merge_fretboard_data(fretboard_notes, fretboard_coordinates)

# Generate all triads and display
all_triads_positions = generate_all_triads(merged_fretboard_notes)
for key, value in all_triads_positions.items():
    print(f"{key}: {value}")
print(len(merged_fretboard_notes))

# Saving generated triads to a file
def save_triads_to_file(file_name, triads_data):
    with open(file_name, "w") as file:
        file.write("# Auto-generated file containing triads map\n\n")
        file.write("generated_triads_map = {\n")
        for key, value in triads_data.items():
            file.write(f"    {repr(key)}: {repr(value)},\n")
        file.write("}\n")

# Save the generated triads map
save_triads_to_file("generated_triads_map.py", all_triads_positions)
print("Triads map has been saved to generated_triads_map.py")