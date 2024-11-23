# Given fretboard dictionary
fretboard_notes = {
    ('string_1', 'fret_0'): ('E', 4, (178, 139, 90, 255), (-72.0, 2)),
    ('string_1', 'fret_1'): ('F', 4, (84, 116, 143, 255), (76.0, 2)),
    ('string_2', 'fret_0'): ('B', 3, (54, 80, 71, 255), (-72.0, 112)),
    ('string_2', 'fret_1'): ('C', 4, (20, 55, 85, 255), (76.0, 112)),
    ('string_3', 'fret_0'): ('G', 3, (153, 25, 43, 255), (-72.0, 222)),
    ('string_3', 'fret_2'): ('A', 3, (216, 158, 15, 255), (76.0, 222)),
    ('string_4', 'fret_2'): ('E', 3, (178, 139, 90, 255), (76.0, 332)),
    ('string_5', 'fret_3'): ('C', 3, (20, 55, 85, 255), (76.0, 442)),
    # Add more notes as needed
}

# Define the C major triad and its inversions
c_major_triads = {
    "root": ("C", "E", "G"),
    "1st_inversion": ("E", "G", "C"),
    "2nd_inversion": ("G", "C", "E"),
}

# Function to find detailed positions for triad notes
def find_detailed_positions(fretboard_notes, triad_notes):
    detailed_positions = {note: [] for note in triad_notes}
    for position, (note, octave, color, coordinates) in fretboard_notes.items():
        if note in triad_notes:
            string, fret = position
            detailed_positions[note].append((note, string, fret, octave, coordinates))
    return detailed_positions

# Organize C major triads across string sets with detailed info
triad_detailed_dict = {}
string_sets = ["123", "234", "345", "456"]

for string_set in string_sets:
    for inversion_name, notes in c_major_triads.items():
        # Find detailed positions for each note in the current inversion
        positions = find_detailed_positions(fretboard_notes, notes)
        
        # Get the notes in order based on the inversion
        triad_detailed_dict[("major", "C", string_set, inversion_name)] = tuple(
            positions[note][0] for note in notes  # Get the first occurrence of each note
        )

# Display the structured dictionary
for key, value in triad_detailed_dict.items():
    print(f"{key}: {value}")
