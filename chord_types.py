interval_to_semitones = {
    "1": {"name": "unison", "semitones": 0},
    "b2": {"name": "minor_second", "semitones": 1},
    "2": {"name": "major_second", "semitones": 2},
    "b3": {"name": "minor_third", "semitones": 3},
    "3": {"name": "major_third", "semitones": 4},
    "4": {"name": "perfect_fourth", "semitones": 5},
    "#4": {"name": "augmented_fourth", "semitones": 6},
    "b5": {"name": "diminished_fifth", "semitones": 6},
    "5": {"name": "perfect_fifth", "semitones": 7},
    "#5": {"name": "minor_sixth", "semitones": 8},
    "b6": {"name": "minor_sixth", "semitones": 8},
    "6": {"name": "major_sixth", "semitones": 9},
    "bb7": {"name": "diminished_seventh", "semitones": 9},
    "#6": {"name": "minor_seventh", "semitones": 10},
    "b7": {"name": "minor_seventh", "semitones": 10},
    "7": {"name": "major_seventh", "semitones": 11},
    "8": {"name": "octave", "semitones": 12},
    "b9": {"name": "minor_ninth", "semitones": 13},
    "9": {"name": "major_ninth", "semitones": 14},
    "#9": {"name": "minor_tenth", "semitones": 15},
    "b10": {"name": "minor_tenth", "semitones": 15},
    "10": {"name": "major_tenth", "semitones": 16},
    "11": {"name": "perfect_eleventh", "semitones": 17},
    "#11": {"name": "augmented_eleventh", "semitones": 18},
    "12": {"name": "perfect_twelfth", "semitones": 19},
    "b13": {"name": "minor_thirteenth", "semitones": 20},
    "13": {"name": "major_thirteenth", "semitones": 21},
    "b14": {"name": "minor_fourteenth", "semitones": 22},
    "14": {"name": "major_fourteenth", "semitones": 23},
    "15": {"name": "double_octave", "semitones": 24},
}

chord_voicings = {
    "closed_triad": [
        [1, 2, 3],  # Strings 1, 2, and 3
        [2, 3, 4],  # Strings 2, 3, and 4
        [3, 4, 5],  # Strings 3, 4, and 5
        [4, 5, 6],  # Strings 4, 5, and 6
    ],
    "closed_4note": [
        [1, 2, 3, 4],  # Strings 1, 2, 3, and 4
        [2, 3, 4, 5],  # Strings 2, 3, 4, and 5
        [3, 4, 5, 6],  # Strings 3, 4, 5, and 6
    ],
    "drop_2": [
        [1, 2, 3, 4],  # Strings 1, 2, 3, and 4
        [2, 3, 4, 5],  # Strings 2, 3, 4, and 5
        [3, 4, 5, 6],  # Strings 3, 4, 5, and 6
    ],
    "drop_3": [
        [1, 2, 3, 5],  # Strings 1, 2, 3, and 5
        [2, 3, 4, 6],  # Strings 2, 3, 4, and 6
    ],
    "drop_2_and_4": [
        [1, 2, 4, 5],  # Strings 1, 2, 4, and 5
        [2, 3, 5, 6],  # Strings 2, 3, 5, and 6
    ],
    "drop_2_and_3": [
        [1, 2, 4, 6],  # Strings 1, 2, 4, and 6
    ],
}

chord_types = {
    'Diminished': {'Symbols': ['°', 'mb5', '-b5', 'dim'], 'Function': ['1', 'b3', 'b5'], 'PossibleVoicings': ['closed_triad']}, 
    'Minor': {'Symbols': ['m', '-', 'min'], 'Function': ['1', 'b3', '5'], 'PossibleVoicings': ['closed_triad']}, 
    'Major': {'Symbols': ['M', 'maj'], 'Function': ['1', '3', '5'], 'PossibleVoicings': ['closed_triad']}, 
    'Augmented': {'Symbols': ['+', 'aug', '#5'], 'Function': ['1', '3', '#5'], 'PossibleVoicings': ['closed_triad']}, 
    'sus2': {'Symbols': ['sus2'], 'Function': ['1', '2', '5'], 'PossibleVoicings': ['closed_triad']}, 
    'sus4': {'Symbols': ['sus4'], 'Function': ['1', '4', '5'], 'PossibleVoicings': ['closed_triad']}, 
    'Major (b5)': {'Symbols': ['(b5)', 'Mb5', 'Maj-5'], 'Function': ['1', '3', 'b5'], 'PossibleVoicings': ['closed_triad']}, 
    'Diminished seventh': {'Symbols': ['°7', 'dim7'], 'Function': ['1', 'b3', 'b5', 'bb7'], 'PossibleVoicings': ['closed_4note', 'drop_2', 'drop_3', 'drop_2_and_4', 'drop_2_and_3']}, 
    'Half diminished': {'Symbols': ['Ø', 'm7b5', '-7b5', 'min7b5', 'mi7b5'], 'Function': ['1', 'b3', 'b5', 'b7'], 'PossibleVoicings': ['closed_4note', 'drop_2', 'drop_3', 'drop_2_and_4', 'drop_2_and_3']}, 
    'Minor seventh': {'Symbols': ['m7', '-7', 'min7', 'mi7'], 'Function': ['1', 'b3', '5', 'b7'], 'PossibleVoicings': ['closed_4note', 'drop_2', 'drop_3', 'drop_2_and_4', 'drop_2_and_3']}, 
    'Minor major seventh': {'Symbols': ['mΔ', '-Δ', 'minΔ', 'miΔ', 'minMaj7', 'mMaj7'], 'Function': ['1', 'b3', '5', '7'], 'PossibleVoicings': ['closed_4note', 'drop_2', 'drop_3', 'drop_2_and_4', 'drop_2_and_3']}, 
    'Dominant seventh': {'Symbols': ['7', 'dom7'], 'Function': ['1', '3', '5', 'b7'], 'PossibleVoicings': ['closed_4note', 'drop_2', 'drop_3', 'drop_2_and_4', 'drop_2_and_3']}, 
    'Major seventh': {'Symbols': ['Δ', 'Maj7', 'Ma7', 'M7'], 'Function': ['1', '3', '5', '7'], 'PossibleVoicings': ['closed_4note', 'drop_2', 'drop_3', 'drop_2_and_4', 'drop_2_and_3']}, 
    'Major seventh raised fifth': {'Symbols': ['Δ+', 'Δ#5', 'Maj7#5', 'Maj7+'], 'Function': ['1', '3', '#5', '7'], 'PossibleVoicings': ['closed_4note', 'drop_2', 'drop_3', 'drop_2_and_4', 'drop_2_and_3']}, 
    'Altered dominant': {'Symbols': ['7+', '7#5', '7alt'], 'Function': ['1', '3', '#5', 'b7'], 'PossibleVoicings': ['closed_4note', 'drop_2', 'drop_3', 'drop_2_and_4', 'drop_2_and_3']}, 
    'Dominant with flattened fifth': {'Symbols': ['7b5'], 'Function': ['1', '3', 'b5', 'b7'], 'PossibleVoicings': ['closed_4note', 'drop_2', 'drop_3', 'drop_2_and_4', 'drop_2_and_3']}, 
    'Major seventh with flattened fifth': {'Symbols': ['Δb5', 'Maj7b5'], 'Function': ['1', '3', 'b5', '7'], 'PossibleVoicings': ['closed_4note', 'drop_2', 'drop_3', 'drop_2_and_4', 'drop_2_and_3']}, 
    'Dominant thirteenth': {'Symbols': ['13', 'dom13'], 'Function': ['1', '3', '5', 'b7', '9', '11', '13'], 'PossibleVoicings': ['drop_2_and_4', 'drop_2_and_3']}, 
    'Major thirteenth': {'Symbols': ['Maj13', 'Δ13'], 'Function': ['1', '3', '5', '7', '9', '11', '13'], 'PossibleVoicings': ['drop_2_and_4', 'drop_2_and_3']}, 
    'Minor thirteenth': {'Symbols': ['m13', '-13', 'min13'], 'Function': ['1', 'b3', '5', 'b7', '9', '11', '13'], 'PossibleVoicings': ['drop_2_and_4', 'drop_2_and_3']}, 
    'Half-diminished thirteenth': {'Symbols': ['m7b5/13', 'Ø13'], 'Function': ['1', 'b3', 'b5', 'b7', '9', '11', '13'], 'PossibleVoicings': ['drop_2_and_4', 'drop_2_and_3']}, 
    'Diminished thirteenth': {'Symbols': ['dim13', '°13'], 'Function': ['1', 'b3', 'b5', 'bb7', '9', '11', '13'], 'PossibleVoicings': ['drop_2_and_4', 'drop_2_and_3']}, 
    'Dominant eleventh': {'Symbols': ['11', 'dom11'], 'Function': ['1', '3', '5', 'b7', '9', '11'], 'PossibleVoicings': ['drop_2_and_4', 'drop_2_and_3']}, 
    'Major eleventh': {'Symbols': ['Maj11', 'Δ11'], 'Function': ['1', '3', '5', '7', '9', '11'], 'PossibleVoicings': ['drop_2_and_4', 'drop_2_and_3']}, 
    'Minor eleventh': {'Symbols': ['m11', '-11', 'min11'], 'Function': ['1', 'b3', '5', 'b7', '9', '11'], 'PossibleVoicings': ['drop_2_and_4', 'drop_2_and_3']}, 
    'Suspended ninth': {'Symbols': ['sus9'], 'Function': ['1', '4', '5', 'b7', '9'], 'PossibleVoicings': ['drop_2_and_4', 'drop_2_and_3']}, 
    'Dominant flat nine': {'Symbols': ['7♭9'], 'Function': ['1', '3', '5', 'b7', 'b9'], 'PossibleVoicings': ['drop_2_and_4', 'drop_2_and_3']}, 
    'Dominant sharp nine': {'Symbols': ['7♯9'], 'Function': ['1', '3', '5', 'b7', '#9'], 'PossibleVoicings': ['drop_2_and_4', 'drop_2_and_3']}, 
    'Dominant flat thirteen': {'Symbols': ['7♭13'], 'Function': ['1', '3', '5', 'b7', 'b13'], 'PossibleVoicings': ['drop_2_and_4', 'drop_2_and_3']}, 
    'Dominant sharp thirteen': {'Symbols': ['7♯13'], 'Function': ['1', '3', '5', 'b7', '#13'], 'PossibleVoicings': ['drop_2_and_4', 'drop_2_and_3']}, 
    'Fully altered dominant': {'Symbols': ['7alt', '7♭9♯9♯5♭5'], 'Function': ['1', '3', '#5', 'b7', 'b9', '#9'], 'PossibleVoicings': ['drop_2_and_4', 'drop_2_and_3']}, 
    'Diminished ninth': {'Symbols': ['dim9', '°9'], 'Function': ['1', 'b3', 'b5', 'bb7', '9'], 'PossibleVoicings': ['drop_2_and_4', 'drop_2_and_3']}, 
    'Quartal triad': {'Symbols': ['quartal'], 'Function': ['1', '4', '7'], 'PossibleVoicings': ['closed_triad']}, 
    'Polychord': {'Symbols': ['C/G', 'D/F#'], 'Function': ['Two triads played together (e.g., C major with G major)'], 'PossibleVoicings': []}, 
    'Cluster chord': {'Symbols': ['cluster'], 'Function': ["Adjacent notes (e.g., 'C-D-E')"], 'PossibleVoicings': []}, 
    'Major sixth': {'Symbols': ['6', 'Maj6'], 'Function': ['1', '3', '5', '6'], 'PossibleVoicings': ['closed_4note', 'drop_2', 'drop_3', 'drop_2_and_4', 'drop_2_and_3']}, 
    'Minor sixth': {'Symbols': ['m6', '-6', 'min6'], 'Function': ['1', 'b3', '5', '6'], 'PossibleVoicings': ['closed_4note', 'drop_2', 'drop_3', 'drop_2_and_4', 'drop_2_and_3']}, 
    'Add9': {'Symbols': ['add9'], 'Function': ['1', '3', '5', '9'], 'PossibleVoicings': ['closed_4note', 'drop_2', 'drop_3', 'drop_2_and_4', 'drop_2_and_3']}, 
    'Add11': {'Symbols': ['add11'], 'Function': ['1', '3', '5', '11'], 'PossibleVoicings': ['closed_4note', 'drop_2', 'drop_3', 'drop_2_and_4', 'drop_2_and_3']}, 
    'Slash chord': {'Symbols': ['C/E', 'G/B'], 'Function': ["Specify a non-root bass note (e.g., 'C/E' means C major chord with E in the bass)"], 'PossibleVoicings': []}, 
    'Minor ninth': {'Symbols': ['min9', '-9'], 'Function': ['1', 'b3', '5', 'b7', '9'], 'PossibleVoicings': ['drop_2_and_4', 'drop_2_and_3']}, 
    'Dominant minor ninth': {'Symbols': ['7b9'], 'Function': ['1', '3', '5', 'b7', 'b9'], 'PossibleVoicings': ['drop_2_and_4', 'drop_2_and_3']}
}

#service functions

def get_chord_types():
    chords = list(chord_types.keys())
    return chords

def get_chord_intervals(chord):
    return chord_types[chord]["Function"]
     

def get_chord_Symbols(chord):
    return chord_types[chord]["Symbols"]



chromatic_scale_sharp = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
chromatic_scale_flat = ["C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab", "A", "Bb", "B"]

def build_chord(chord_type, key, octave, chord_definitions):
    """
    Build a chord based on the chord type, root key, and octave.
    
    Args:
        chord_type (str): The type of chord (e.g., "Diminished").
        key (str): The root note (e.g., "E").
        octave (int): The octave for the root note (e.g., 4).
        chord_definitions (dict): Dictionary with chord types, symbols, and functions.
        
    Returns:
        dict: A dictionary with the chord name and the generated chord notes.
    """
    # Get the chord definition
    chord_data = chord_definitions.get(chord_type)
    if not chord_data:
        return {"error": f"Chord type '{chord_type}' not found."}

    # Retrieve the intervals from the Function list
    intervals = chord_data["Function"]

    # Determine the appropriate chromatic scale based on the root note
    if key in chromatic_notes_flat:
        scale = chromatic_notes_flat
    elif key in chromatic_notes_sharp:
        scale = chromatic_notes_sharp
    else:
        return {"error": f"Root note '{key}' is not valid."}

    # Find the root index in the chromatic scale
    root_index = scale.index(key)

    # Build the chord
    chord_notes = [key+str(octave)]
    for interval in intervals:
        if interval == "1":
            continue
        if "b" in interval:
            scale = chromatic_scale_flat
        else:
            scale = chromatic_scale_sharp


        # Map the interval to semitones
        semitones = interval_to_semitones[interval]["semitones"]
        # Calculate the note index in the chromatic scale
        note_index = (root_index + semitones) % 12
        # Calculate the octave shift
        octave_shift = (root_index + semitones) // 12
        # Append the note and octave
        chord_notes.append(f"{scale[note_index]}{octave + octave_shift}")

    # Determine the chord name using the first symbol, excluding the pitch
    chord_symbol = chord_data["Symbols"][0]
    chord_name = f"{key}{chord_symbol}"

    return {"chord_name": chord_name, "chord_notes": chord_notes, "intervals": intervals}




chromatic_notes_flat = ["C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab", "A", "Bb", "B"]
chromatic_notes_sharp = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]

"""
    Searches for the index of a note in the chromatic notes (flat and sharp lists).

"""
def find_note_index(note):
    if note in chromatic_notes_flat:
        return chromatic_notes_flat.index(note)
    elif note in chromatic_notes_sharp:
        return chromatic_notes_sharp.index(note)
    else:
        return -1
    

def generate_inversions(chord_notes, root_pitch,chord_type='major'):
    """
    Generate chord inversions for a chord with any number of notes, accounting for chromatic scale.

    Parameters:
    chord_notes (list): List of notes in the chord (e.g., ['C', 'E', 'G', 'B']).
    root_pitch (int): The pitch number of the root note (e.g., 4 for C4).

    Returns:
    list: List of inversions, each containing notes with their pitches.
    """
    
    # Initialize the root position
    inversions = []
    pitches = [root_pitch]  # Start with the root pitch

    # Assign pitches based on the chromatic scale and root note
    root_index = find_note_index(chord_notes[0])  # Index of root in chromatic scale
    for i in range(1, len(chord_notes)):
        current_index = find_note_index(chord_notes[i])
        # If the current note is "lower" in the chromatic scale, it wraps to the next octave
        if current_index < find_note_index(chord_notes[i - 1]):
            pitches.append(pitches[i - 1] + 1)  # Move to the next octave
        else:
            pitches.append(pitches[i - 1])  # Stay in the same octave

    # Add the root position to inversions
    inversions.append(list(zip(chord_notes, pitches)))

    # Generate inversions by rotating the notes
    for _ in range(len(chord_notes) - 1):
        # Move the first note up an octave
        first_note, first_pitch = inversions[-1][0]
        rest_of_notes = inversions[-1][1:]  # Remaining notes
        new_inversion = rest_of_notes + [(first_note, first_pitch + 1)]
        inversions.append(new_inversion)

    return inversions



def strip_notes(chord):
    clean_chord=[]
    for note in chord:
        if len(note) == 2:
            clean_chord.append(note[0])
        if len(note) > 2:
            clean_chord.append(note[0]+note[1])
    return clean_chord

def chord_with_inversions(chord_type, key, octave, chord_types):
    result = {}
    result['Type'] = chord_type
    the_chord = build_chord(chord_type, key, octave, chord_types)
    #print("the chord",the_chord)
    result.update(the_chord)
    stripNotes = strip_notes(result['chord_notes'])
    if len(result['chord_notes'][0]) == 2:
        root_pitch = int(result['chord_notes'][0][1]) 
    else:
        root_pitch = int(result['chord_notes'][0][2])
    #print(root_pitch)
    inversions = generate_inversions(stripNotes, root_pitch, chord_type='major')
    result['Inverions'] = inversions
    """
    for idx, inversion in enumerate(inversions):
        print(f"Inversion {idx + 1}: {inversion}")
    """
    return result



"""
    Objects are made immutable to ensure consistent hash values, 
    enabling efficient and reliable uniqueness checks in hash-based 
    collections like sets or dictionaries.
"""
from collections import OrderedDict
def make_immutable(obj):
    """Recursively convert mutable objects to immutable equivalents, preserving order."""
    if isinstance(obj, dict):
        # Convert dict to tuple of ordered key-value pairs
        return tuple((k, make_immutable(v)) for k, v in obj.items())
    elif isinstance(obj, list):
        # Convert list to tuple
        return tuple(make_immutable(item) for item in obj)
    elif isinstance(obj, tuple):
        # Convert each element of the tuple
        return tuple(make_immutable(item) for item in obj)
    else:
        # Leave immutable objects (str, int, float, etc.) as they are
        return obj



# Example usage
chord_type = "Major"
key = "G"
octave = 4


#print(chord_with_inversions(chord_type, key, octave, chord_types))

def chord_with_inversions_immutable(chord_type, key, octave, chord_types):
    data = chord_with_inversions(chord_type, key, octave, chord_types)
    #print(data)
    return make_immutable(data)


#print(chord_with_inversions_immutable(chord_type, key, octave, chord_types))

