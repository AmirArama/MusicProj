
chord_types = {
    'Diminished': {'Symbols': ['°', 'mb5', '-b5', 'dim'], 'Function': ['1', 'b3', 'b5']}, 
    'Minor': {'Symbols': ['m', '-', 'min'], 'Function': ['1', 'b3', '5']}, 
    'Major': {'Symbols': ['M', 'maj'], 'Function': ['1', '3', '5']}, 
    'Augmented': {'Symbols': ['+', 'aug', '#5'], 'Function': ['1', '3', '#5']}, 
    'sus2': {'Symbols': ['sus2'], 'Function': ['1', '2', '5']}, 
    'sus4': {'Symbols': ['sus4'], 'Function': ['1', '4', '5']}, 
    'Major (b5)': {'Symbols': ['(b5)', 'Mb5', 'Maj-5'], 'Function': ['1', '3', 'b5']}, 
    'Diminished seventh': {'Symbols': ['°7', 'dim7'], 'Function': ['1', 'b3', 'b5', 'bb7']}, 
    'Half diminished': {'Symbols': ['Ø', 'm7b5', '-7b5', 'min7b5', 'mi7b5'], 'Function': ['1', 'b3', 'b5', 'b7']}, 
    'Minor seventh': {'Symbols': ['m7', '-7', 'min7', 'mi7'], 'Function': ['1', 'b3', '5', 'b7']}, 
    'Minor major seventh': {'Symbols': ['mΔ', '-Δ', 'minΔ', 'miΔ', 'minMaj7', 'mMaj7'], 'Function': ['1', 'b3', '5', '7']}, 
    'Dominant seventh': {'Symbols': ['7', 'dom7'], 'Function': ['1', '3', '5', 'b7']}, 
    'Major seventh': {'Symbols': ['Δ', 'Maj7', 'Ma7', 'M7'], 'Function': ['1', '3', '5', '7']}, 
    'Major seventh raised fifth': {'Symbols': ['Δ+', 'Δ#5', 'Maj7#5', 'Maj7+'], 'Function': ['1', '3', '#5', '7']}, 
    'Altered dominant': {'Symbols': ['7+', '7#5', '7alt'], 'Function': ['1', '3', '#5', 'b7']}, 
    'Dominant with flattened fifth': {'Symbols': ['7b5'], 'Function': ['1', '3', 'b5', 'b7']}, 
    'Major seventh with flattened fifth': {'Symbols': ['Δb5', 'Maj7b5'], 'Function': ['1', '3', 'b5', '7']}, 
    'Dominant thirteenth': {'Symbols': ['13', 'dom13'], 'Function': ['1', '3', '5', 'b7', '9', '11', '13']}, 
    'Major thirteenth': {'Symbols': ['Maj13', 'Δ13'], 'Function': ['1', '3', '5', '7', '9', '11', '13']}, 
    'Minor thirteenth': {'Symbols': ['m13', '-13', 'min13'], 'Function': ['1', 'b3', '5', 'b7', '9', '11', '13']}, 
    'Half-diminished thirteenth': {'Symbols': ['m7b5/13', 'Ø13'], 'Function': ['1', 'b3', 'b5', 'b7', '9', '11', '13']}, 
    'Diminished thirteenth': {'Symbols': ['dim13', '°13'], 'Function': ['1', 'b3', 'b5', 'bb7', '9', '11', '13']}, 
    'Dominant eleventh': {'Symbols': ['11', 'dom11'], 'Function': ['1', '3', '5', 'b7', '9', '11']}, 
    'Major eleventh': {'Symbols': ['Maj11', 'Δ11'], 'Function': ['1', '3', '5', '7', '9', '11']}, 
    'Minor eleventh': {'Symbols': ['m11', '-11', 'min11'], 'Function': ['1', 'b3', '5', 'b7', '9', '11']}, 
    'Suspended ninth': {'Symbols': ['sus9'], 'Function': ['1', '4', '5', 'b7', '9']}, 
    'Dominant flat nine': {'Symbols': ['7♭9'], 'Function': ['1', '3', '5', 'b7', 'b9']}, 
    'Dominant sharp nine': {'Symbols': ['7♯9'], 'Function': ['1', '3', '5', 'b7', '#9']}, 
    'Dominant flat thirteen': {'Symbols': ['7♭13'], 'Function': ['1', '3', '5', 'b7', 'b13']}, 
    'Dominant sharp thirteen': {'Symbols': ['7♯13'], 'Function': ['1', '3', '5', 'b7', '#13']}, 
    'Fully altered dominant': {'Symbols': ['7alt', '7♭9♯9♯5♭5'], 'Function': ['1', '3', '#5', 'b7', 'b9', '#9']}, 
    'Diminished ninth': {'Symbols': ['dim9', '°9'], 'Function': ['1', 'b3', 'b5', 'bb7', '9']}, 
    'Quartal triad': {'Symbols': ['quartal'], 'Function': ['1', '4', '7']}, 
    'Polychord': {'Symbols': ['C/G', 'D/F#'], 'Function': ['Two triads played together (e.g., C major with G major)']}, 
    'Cluster chord': {'Symbols': ['cluster'], 'Function': ["Adjacent notes (e.g., 'C-D-E')"]}, 
    'Major sixth': {'Symbols': ['6', 'Maj6'], 'Function': ['1', '3', '5', '6']}, 
    'Minor sixth': {'Symbols': ['m6', '-6', 'min6'], 'Function': ['1', 'b3', '5', '6']}, 
    'Add9': {'Symbols': ['add9'], 'Function': ['1', '3', '5', '9']}, 
    'Add11': {'Symbols': ['add11'], 'Function': ['1', '3', '5', '11']}, 
    'Slash chord': {'Symbols': ['C/E', 'G/B'], 'Function': ["Specify a non-root bass note (e.g., 'C/E' means C major chord with E in the bass)"]}, 
    'Minor ninth': {'Symbols': ['min9', '-9'], 'Function': ['1', 'b3', '5', 'b7', '9']}, 
    'Dominant minor ninth': {'Symbols': ['7b9'], 'Function': ['1', '3', '5', 'b7', 'b9']}
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


def enhance_chord_data(chord_types, chord_voicings):

    # Enhance each chord in the dictionary
    for chord, data in chord_types.items():
        num_notes = len(data["Function"])
        possible_voicings = []
        if num_notes == 3:  # Triad
            possible_voicings.append("closed_triad")
        if num_notes == 4:  # 4-note chord
            possible_voicings.extend(["closed_4note", "drop_2", "drop_3"])
        if num_notes >= 4:  # Extended chords with at least 4 notes
            possible_voicings.extend(["drop_2_and_4", "drop_2_and_3"])

        data["PossibleVoicings"] = possible_voicings

    return chord_types


enhanced_chord_types = enhance_chord_data(chord_types, chord_voicings)

# Print the updated dictionary
#import pprint
#pprint.pprint(enhanced_chord_types)

print(enhanced_chord_types)
