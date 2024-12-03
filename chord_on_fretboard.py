from chord_positions import *
from chord_types import *


#print(notes_22frets_sharp)
#print(notes_22frets_flat) 


def find_inversions_positions(the_chord, string_set):
    chord_inversions_notes = the_chord['Inverions']
    inversionsDic = {}
    for idx,inversion in enumerate(chord_inversions_notes):
        #print(inversion)
        inversion_r = inversion[::-1]
        print("~~"*10+"inversions"+"~~"*10)
        #print(inversion_r)
        positions = []
        found_position = True
        for note, string_ in zip(inversion_r, string_set) :
            note_name = note[0]
            note_pitch = note[1]
            #print(note_name,note_pitch)
            frets = []
            if "b" in note_name:
                frets = [(fret,note_name+str(note_pitch)) for fret, n in enumerate(notes_22frets_flat['string'+str(string_)]) if n[0] == note_name and n[1] == str(note_pitch)]
            else:
                frets = [(fret,note_name+str(note_pitch)) for fret, n in enumerate(notes_22frets_sharp['string'+str(string_)]) if n[0] == note_name and n[1] == str(note_pitch)]
            #print(frets)
           
            if not frets:
                found_position = False
            else:
                #positions.append({string_: frets[0]})
                positions.append({
                    "string":string_,
                    "fret":frets[0][0],
                    "note":frets[0][1]})

        if found_position == False:
            print("Inverion can not be placed on the fretboard")
            inversionsDic["inversion_"+str(idx+1)] = "None"
        else:
            #print(idx)
            inversionsDic["inversion_"+str(idx+1)] = positions

            

        print(positions)
    print(inversionsDic)

chord_type = "Diminished seventh"
key = "C"
octave = 3

the_chord = chord_with_inversions(chord_type, key, octave, chord_types)
print(the_chord)

find_inversions_positions(the_chord, [1,2,3,4])

