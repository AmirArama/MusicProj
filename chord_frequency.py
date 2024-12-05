def calculate_fretboard_frequencies(base_notes, num_of_frets, chromatic_scale):
    """
    Calculate the frequency of each note on the fretboard for each string.

    Args:
    - base_notes (list): List of dictionaries containing the base note, its frequency, and octave.
    - num_of_frets (int): Number of frets on the fretboard.
    - chromatic_scale (list): The chromatic scale (sharp or flat).

    Returns:
    - list: A list of dictionaries, where each dictionary represents a string and its notes.
    """
    fretboard = []

    for base_note in base_notes:
        string_notes = []  # To store the notes for the current string
        for fret in range(num_of_frets + 1):
            # Calculate frequency for the current fret
            frequency = base_note["frequency"] * (2 ** (fret / 12))
            # Determine the note and octave
            note_index = (chromatic_scale.index(base_note["note"]) + fret) % 12
            octave = base_note["octave"] + (chromatic_scale.index(base_note["note"]) + fret) // 12
            note = chromatic_scale[note_index]

            # Add the note to the string
            string_notes.append({
                "fret": fret,
                "note": note,
                "frequency": round(frequency, 2),  # Round to 2 decimal places
                "octave": octave
            })
        
        fretboard.append(string_notes)
    
    return fretboard


# Define input data
chromatic_scale_sharp = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
chromatic_scale_flat = ["C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab", "A", "Bb", "B"]

base_notes = [
    { "note": "E", "frequency": 82.41, "octave": 2 },  # E2 (Low E string)
    { "note": "A", "frequency": 110.00, "octave": 2 }, # A2
    { "note": "D", "frequency": 146.83, "octave": 3 }, # D3
    { "note": "G", "frequency": 196.00, "octave": 3 }, # G3
    { "note": "B", "frequency": 246.94, "octave": 3 }, # B3
    { "note": "E", "frequency": 329.63, "octave": 4 }, # E4 (High E string)
]

base_notes = [
    { "note": "E", "frequency": 329.63, "octave": 4 }, # E4 (High E string)
    { "note": "B", "frequency": 246.94, "octave": 3 }, # B3
    { "note": "G", "frequency": 196.00, "octave": 3 }, # G3
    { "note": "D", "frequency": 146.83, "octave": 3 }, # D3
    { "note": "A", "frequency": 110.00, "octave": 2 }, # A2
    { "note": "E", "frequency": 82.41, "octave": 2 },  # E2 (Low E string)
]

num_of_frets = 22

# Calculate fretboard frequencies


# Print all strings and their notes
def create_frequency_dic(chromatic_scale):
    fretboard = calculate_fretboard_frequencies(base_notes, num_of_frets, chromatic_scale)
    tmplist = []
    for i, string_notes in enumerate(fretboard):
        #print(f"String {i + 1}:")
        for note_info in string_notes:
            fret = note_info['fret']
            frequency = note_info['frequency']
            ent = {"string":i+1,"fret":fret,"frequency":frequency}
            tmplist.append(ent)
    return tmplist

"""
x = create_frequency_dic(chromatic_scale_sharp)
print(x)
"""