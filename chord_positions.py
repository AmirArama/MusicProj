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

def rearange_the_fretbpard_dic(old_presentation):
    x_keys = list(old_presentation.keys())
    x_values = list(old_presentation.values())
    notes_22frets_r = []
    for i,string in enumerate(x_keys):
        #print(i,string)
        #print(x_values[i])
        for j,note in enumerate(x_values[i]):
            notes_22frets_r.append(
                {
                    "string":i+1,
                    "fret": j,
                    "note": note[0],
                    "octave": note[1]
                }
            )
    return notes_22frets_r
        
notes_22frets_sharp_r = rearange_the_fretbpard_dic(notes_22frets_sharp)
notes_22frets_flat_r = rearange_the_fretbpard_dic(notes_22frets_flat)

# A Sneaky Bug Fix
# In some cases, the first inversion found on the fretboard is not the root inversion. 
# This happens when the notes needed to build the root inversion are missing on the fretboard. 
# As a result, it becomes impossible to produce and position subsequent inversions correctly.
# 
# By supplying virtual notes outside the physical fretboard range, we address this issue, 
# ensuring that all inversions can be calculated and placed properly.

fake_notes_sharp = [
    # Virtual notes for octave 2 on lower strings
    {'string': 6, 'fret': -1, 'note': 'C', 'octave': '2'},
    {'string': 6, 'fret': -1, 'note': 'C#', 'octave': '2'},
    {'string': 6, 'fret': -1, 'note': 'D', 'octave': '2'},
    {'string': 6, 'fret': -1, 'note': 'D#', 'octave': '2'}
]
fake_notes_flat = [
    # Virtual notes for octave 2 on lower strings
    {'string': 6, 'fret': -1, 'note': 'C', 'octave': '2'},
    {'string': 6, 'fret': -1, 'note': 'Db', 'octave': '2'},
    {'string': 6, 'fret': -1, 'note': 'D', 'octave': '2'},
    {'string': 6, 'fret': -1, 'note': 'Eb', 'octave': '2'}
]
notes_22frets_sharp_r = notes_22frets_sharp_r + fake_notes_sharp
notes_22frets_flat_r = notes_22frets_flat_r + fake_notes_flat

#print("aaaaaaaa"*20)
#print (notes_22frets_flat_r)

def get_a_note_on_fterboard(note):
    notes = notes_22frets_flat_r
    if len(note) == 2 and note[1] == "#":
        notes = notes_22frets_sharp_r
    fnotes = []
    for idx in notes:
        if idx["note"] == note:
            fnotes.append(idx)
    return fnotes

#enote = get_a_note_on_fterboard("E")
#print(enote)