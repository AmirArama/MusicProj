from chord_positions import *
from chord_types import *

"""
    In this file: 
    1. Build the chord based on its interval recipe from left to right. 
       This is your theoretical formula, which creates the chord intervals in order 
       (e.g., root, third, fifth).

    2. Reverse the chord to make the root position on the bass. 
       This involves rearranging the notes so that the root appears as the lowest note. 
"""


"""
    function input: 
    1. The chors and all for the inversions
    2. The string set the chord can be found at e.g., for traids 123,234,345,456 
    3. the vord is in a speciffic root pitch e.g., E4 is the pitch E Major is the chord 
    founction output:
    if the chord can be placed on the fretboard the chord notes string, fret and pitch for each note 
    and for each inversion 
    Note: for some chords as expected only subset of inversions are posible (including the root)  
"""
def find_inversions_positions(the_chord, string_set):
    
    # Chord with all inversions based on its interval recipe from left to right. 
    chord_inversions_notes = the_chord['Inverions']
    inversionsDic = {}
    inversionsDic["chord info"] = the_chord
    inversionsDic["string set"] = string_set

    for idx,inversion in enumerate(chord_inversions_notes):

        # Reverse the chord to make the root position on the bass.
        inversion_r = inversion[::-1]
        
        positions = []
        found_position = True
        for note, string_ in zip(inversion_r, string_set) :
            
            note_name = note[0]
            note_pitch = note[1]
            frets = []

            if "b" in note_name:
                frets = [(fret,note_name+str(note_pitch)) for fret, n in enumerate(notes_22frets_flat['string'+str(string_)]) if n[0] == note_name and n[1] == str(note_pitch)]
            else:
                frets = [(fret,note_name+str(note_pitch)) for fret, n in enumerate(notes_22frets_sharp['string'+str(string_)]) if n[0] == note_name and n[1] == str(note_pitch)]
           
            if not frets:
                found_position = False
            else:
                positions.append({
                    "string":string_,
                    "fret":frets[0][0],
                    "note":frets[0][1]})

        if found_position == False:
            # In case the inverion can not be placed on the fretboard
            inversionsDic["fb_inversion_"+str(idx+1)] = "None"
        else:
            #print(idx)
            inversionsDic["fb_inversion_"+str(idx+1)] = positions

    return inversionsDic



chord_type = "Diminished seventh"
key = "C"
octave = 3

the_chord = chord_with_inversions(chord_type, key, octave, chord_types)

voicings = chord_voicings["closed_4note"]

for voicing in voicings:

    inversions = find_inversions_positions(the_chord, voicing)
    print("~~o"*20)
    print(inversions)

