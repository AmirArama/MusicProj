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

interval_to_name = {
    "1": "R",
    "b2": "b_flat",
    "2": "2",
    "b3": "3_flat",
    "3": "3",
    "4": "4",
    "#4": "4_sharp",
    "b5": "5_flat",
    "5": "5",
    "#5": "5_flat",
    "b6": "6_flat",
    "6": "6",
    "bb7": "7_flat_flat",
    "#6": "6_sharp",
    "b7": "7_flat",
    "7": "7",
    "8": "8",
    "b9": "9_flat",
    "9": "9",
    "#9": "9_sharp",
    "b10": "10_flat",
    "10": "10",
    "11": "11",
    "#11": "11_sharp",
    "12": "12",
    "b13": "13_flat",
    "13": "13",
    "b14": "14_flat",
    "14": "14",
    "15": "15"
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

def generate_inversions(chord_notes, intervals, root_pitch, applyD2, applyD3, applyD24, chord_type='major'):
    """
    Generate chord inversions for a chord with any number of notes, producing results as lists of notes with their pitches.

    Parameters:
    chord_notes (list): List of notes in the chord (e.g., ['C', 'E', 'G', 'B']).
    root_pitch (int): The pitch number of the root note (e.g., 4 for C4).

    Returns:
    list: List of inversions, each as a list of notes with their pitches (e.g., ['G4', 'C5', 'E3']).
    """

    print("in here drops = ",applyD2, applyD3, applyD24)

    # Initialize the root position
    inversionDic = {}
    inversionDicIn = {}
    inversions = []
    inversionsIn = []
    pitches = [root_pitch]  # Start with the root pitch

    # Assign pitches based on the chromatic scale and root note
    root_index = find_note_index(chord_notes[0])  # Index of root in chromatic scale
    for i in range(1, len(chord_notes)):
        current_index = find_note_index(chord_notes[i])
        # If the current note is "lower" in the chromatic scale, it wraps to the next octave
        if current_index < find_note_index(chord_notes[i - 1]):
            pitches.append(int(pitches[i - 1]) + 1)  # Move to the next octave
        else:
            pitches.append(int(pitches[i - 1]))  # Stay in the same octave

    # Add the root position to inversions
    inversions.append([f"{note}{pitch}" for note, pitch in zip(chord_notes, pitches)])
    inversionDic['root'] = inversions[0]
    inversionsIn.append(intervals)
    inversionDic['root'] = intervals
    #print(inversionsIn)
    for i in range(len(chord_notes) - 1):
        # Move the first note up an octave
        first_note, first_pitch = inversions[-1][0][:-1], int(inversions[-1][0][-1])  # Note and pitch of first note
        rest_of_notes = inversions[-1][1:]  # Remaining notes
        new_inversion = rest_of_notes + [f"{first_note}{first_pitch + 1}"]
        inversions.append(new_inversion)
        inversionDic['inversion'+str(i+1)] =  new_inversion

        intervals = intervals[1:] + intervals[:1]
        #print(intervals)
        #restIn = inversionsIn[-1][1:]
        #newIn = restIn + firstIn
        inversionsIn.append(intervals)

    if applyD2:
        for idx in range(len(inversions)):
            if len(inversions[idx]) > 3:  # Ensure there are enough notes to apply drop 2
                # Drop 2 transformation for notes
                second_highest_note = inversions[idx][-2][:-1]  # Note name of second highest note
                second_highest_pitch = int(inversions[idx][-2][-1])  # Pitch of second highest note
                dropped_note = f"{second_highest_note}{second_highest_pitch - 1}"
                # Adjust the inversion to reflect the dropped note
                inversions[idx] = [dropped_note] + inversions[idx][:-2] + [inversions[idx][-1]]
        
        for idx2 in range(len(inversionsIn)):
            if len(inversions[idx2]) > 3:
                #print("---->", inversionsIn[idx2])

                c = [inversionsIn[idx2][2], inversionsIn[idx2][0], inversionsIn[idx2][1] ,inversionsIn[idx2][3]]
                inversionsIn[idx2] = c
                #print("---->", inversionsIn[idx2])

    if applyD3:
        for idx in range(len(inversions)):
            if len(inversions[idx]) > 3:  # Ensure there are enough notes to apply drop 3
                # Drop 3 transformation for notes
                third_highest_note = inversions[idx][-3][:-1]  # Note name of third-highest note
                third_highest_pitch = int(inversions[idx][-3][-1])  # Pitch of third-highest note
                dropped_note = f"{third_highest_note}{third_highest_pitch - 1}"
                # Adjust the inversion to reflect the dropped note
                inversions[idx] = [dropped_note] + inversions[idx][:-3] + inversions[idx][-2:]

        for idx2 in range(len(inversionsIn)):
            if len(inversions[idx2]) > 3:  # Ensure there are enough intervals for drop 3
                print("Before Drop 3:", inversionsIn[idx2])
                # Rearrange intervals for Drop 3
                c = [inversionsIn[idx2][1], inversionsIn[idx2][0], inversionsIn[idx2][2], inversionsIn[idx2][3]]
                inversionsIn[idx2] = c
                print("After Drop 3:", inversionsIn[idx2])

    
    return inversions, inversionsIn



# Example usage
chord_type = "Diminished seventh"
key = "C"
octave = 4


def build_chord(chord_type, key, chord_definitions):
    """
    Build a chord based on the chord type and root key without pitch.
    
    Args:
        chord_type (str): The type of chord (e.g., "Diminished").
        key (str): The root note (e.g., "E").
        chord_definitions (dict): Dictionary with chord types, symbols, and functions.
        
    Returns:
        dict: A dictionary with the chord name and the generated chord notes (without pitch).
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

    # Build the chord notes (without pitch)
    chord_notes = [key]
    for interval in intervals:
        if interval == "1":
            continue

        # Choose the appropriate scale based on flat/sharp intervals
        if "b" in interval:
            scale = chromatic_notes_flat
        else:
            scale = chromatic_notes_sharp

        # Map the interval to semitones
        semitones = interval_to_semitones[interval]["semitones"]
        # Calculate the note index in the chromatic scale
        note_index = (root_index + semitones) % 12
        # Append the note
        chord_notes.append(scale[note_index])

    # Determine the chord name using the first symbol
    chord_symbol = chord_data["Symbols"][0]
    chord_name = f"{key}{chord_symbol}"

    return {"chord_name": chord_name, "chord_notes": chord_notes, "intervals": intervals}

def chord_with_inversions(chord_type, key, octave, chord_types, applyD2, applyD3, applyD24):
    print("Again -->","applyD2=",applyD2, "applyD3=",applyD3, "applyD24=",applyD24)

    result = {}
    result['Type'] = chord_type
    the_chord = build_chord(chord_type, key, chord_types)
    result.update(the_chord)
    inversions, inversionsIn = generate_inversions(the_chord['chord_notes'], the_chord['intervals'], octave, applyD2, applyD3, applyD24, chord_type='major')
    result['Inverions'] = inversions
    result['InverionsIntervals'] = inversionsIn
    return result




from fretboard_map import get_note_data

string = 5
note_with_octave = 'G#3'




def find_inversions_positions(the_chord, string_set):
    #print(string_set)
    
    inversions_tmp = the_chord['Inverions']
    inversionsIn_tmp = the_chord['InverionsIntervals']

    # Reverse the inversions to make the root position on the bass.
    inversions = []
    for inversion in inversions_tmp:
        inversions.append(inversion[::-1])

    #Do the same for the interval Inversions: Reverse the inversions to make the root position on the bass.
    inversionsIn = []
    for inversionIn in inversionsIn_tmp:
        inversionsIn.append(inversionIn[::-1])

    inversionsDic = {}
    inversionsDic["string set"] = string_set
    inversionsDic["Inverions"] = inversions

    inversions_on_fretboard = {}
    for idx,inversion in enumerate(inversions):
        #print(inversionsIn[idx])
        inversionf = True
        inversion_on_fretboard = []
        string_on_fretboard = []
        for string , note in zip(string_set,inversion):
            note_on_fretboard = get_note_data(string-1,note)
            if note_on_fretboard == None:
                inversionf = False
            else:
                inversion_on_fretboard.append(note_on_fretboard)
                string_on_fretboard.append(string)

        if inversionf == True:
            for  idx2 in range(len(inversion_on_fretboard)):
                inversion_on_fretboard[idx2]["interval"] = inversionsIn[idx][idx2] 
                inversion_on_fretboard[idx2]["jsinterval"] = interval_to_name[inversionsIn[idx][idx2]]

                parts = inversion_on_fretboard[idx2]["jsnote"].split("_")

                the_note = (
                    "string"+str(string_on_fretboard[idx2]) + "_"  
                    + parts[0] #note name 
                    + str(inversion_on_fretboard[idx2]["octave"]) 
                )
                if len(parts) > 1:
                    the_note = the_note + '_' + parts[1]

                inversion_on_fretboard[idx2]["note_sound"] = the_note
            if idx == 0:  
                inversions_on_fretboard['root'] = inversion_on_fretboard
                #print('root inversion found!')       
            else:
                inversions_on_fretboard['inversion'+str(idx)] = inversion_on_fretboard 
                #print('inversion'+str(idx)+' found!')   
            
                  
    if not inversions_on_fretboard:
        return None

    return inversions_on_fretboard

from collections import defaultdict




#y = chord_with_inversions(chord_type, key, octave, chord_types)
#print(y)

#y = find_inversions_positions(y, [1,2,3])
#print(y)
