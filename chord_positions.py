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

chromatic_scale_sharp = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
chromatic_scale_flat = ["C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab", "A", "Bb", "B"]
open_string_notes = [("E",4,4),("B",11,3),("G",7,3),("D",2,3),("A",9,2),("E",4,2)]


fretboardNotes_sharp = {}
fretboardNotes_flat = {}

def generate_strings_notes_22frets(type_):
    global chromatic_scale_sharp
    global chromatic_scale_flat
    if type_=="flat":
        chromatic_notes = chromatic_scale_flat
    elif type_=="sharp":
        chromatic_notes = chromatic_scale_sharp
    else:
        print("fretboard notes type not supported")
        return

    fretboardNotes = {}
    for i in range(6):
        string = []
        startNote = open_string_notes[i][0]
        startNoteIdx = open_string_notes[i][1]
        startOctave = open_string_notes[i][2]
        k = startNoteIdx
        for j in range(23):
            if k%12 == 0:
                k = 0
                startOctave = startOctave + 1
            string.append((chromatic_notes[k],str(startOctave)))
            k = k + 1
        fretboardNotes["string"+str(i+1)] = string
    return fretboardNotes

notes_22frets_sharp = generate_strings_notes_22frets("sharp")
notes_22frets_flat = generate_strings_notes_22frets("flat")

#print(notes_22frets_flat) 
