def rotate_list(lst, shift):
    """Rotate a list to the left by the given shift."""
    return lst[shift:] + lst[:shift]

def generate_major_scale(key, use_flats=True):
    """Generate the major scale for a given key, consistent with the circle of fifths."""
    # Chromatic scales with sharps and flats
    chromatic_sharps = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
    chromatic_flats = ["C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab", "A", "Bb", "B"]
    
    # Use flats or sharps based on the key
    chromatic = chromatic_flats if use_flats else chromatic_sharps

    major_intervals = [2, 2, 1, 2, 2, 2, 1]  # W-W-H-W-W-W-H (whole and half steps)
    
    # Find starting position of the key
    start_idx = chromatic.index(key)
    major_scale = [key]
    
    # Build the major scale using intervals
    for step in major_intervals:
        start_idx = (start_idx + step) % len(chromatic)
        major_scale.append(chromatic[start_idx])
    
    return major_scale

def generate_all_modes(key, use_flats=True):
    """Generate all modes for a given key, consistent with sharps/flats logic."""
    major_scale = generate_major_scale(key, use_flats)
    modes = {
        "Ionian": rotate_list(major_scale, 0),  # No rotation
        "Dorian": rotate_list(major_scale, 1),  # Shift by 1
        "Phrygian": rotate_list(major_scale, 2),  # Shift by 2
        "Lydian": rotate_list(major_scale, 3),  # Shift by 3
        "Mixolydian": rotate_list(major_scale, 4),  # Shift by 4
        "Aeolian": rotate_list(major_scale, 5),  # Shift by 5
        "Locrian": rotate_list(major_scale, 6),  # Shift by 6,
    }
    return modes

# Circle of fifths and sharp/flat preference
circle_of_fifths = [
    ("C", False), ("G", False), ("D", False), ("A", False), ("E", False), ("B", False), 
    ("F#", False), ("Db", True), ("Ab", True), ("Eb", True), ("Bb", True), ("F", True)
]

# Store modes for all keys
def all_modes_generator():
    all_modes = {}
    for key, use_flats in circle_of_fifths:
        all_modes[key] = generate_all_modes(key, use_flats)
    # Display the modes for each key
    for key, modes in all_modes.items():
        print(f"\nKey: {key}")
        for mode, notes in modes.items():
            print(f"  {mode}: {notes}")
    return all_modes


