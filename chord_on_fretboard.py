from chord_positions import *
from chord_types import *
from chord_coordinates import find_coordinates
from chord_frequency import *

"""
    In this file: 
    1. Build the chord based on its interval recipe from left to right. 
       This is your theoretical formula, which creates the chord intervals in order 
       (e.g., root, third, fifth).

    2. Reverse the chord to make the root position on the bass. 
       This involves rearranging the notes so that the root appears as the lowest note. 
"""

chromatic_scale_sharp = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
freq_list = create_frequency_dic(chromatic_scale_sharp)

#Create a name usable for javascript
def process_note_name(note):
    # Check if the note contains a flat or sharp
    if 'b' in note:
        note = note.replace('b', '_flat')
    elif '#' in note:
        note = note.replace('#', '_sharp')
    
    # Remove the number at the end
    note = ''.join([char for char in note if not char.isdigit()])
    
    return note

# Function to find a specific string and fret
def find_frequency(string, fret):
    for entry in freq_list:
        if entry['string'] == string and entry['fret'] == fret:
            return entry['frequency']

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
                x , y = find_coordinates(str(string_), str(frets[0][0]))
                positions.append({
                    "string":string_,
                    "fret":frets[0][0], 
                    "note":frets[0][1],
                    "octave": note_pitch,
                    "x": x,
                    "y": y,
                    "jsname": process_note_name(frets[0][1]),
                    "frequency":find_frequency(string_,frets[0][0])
                    })

        if found_position == False:
            # In case the inverion can not be placed on the fretboard
            inversionsDic["fb_inversion_"+str(idx+1)] = "None"
        else:
            #print(idx)
            inversionsDic["fb_inversion_"+str(idx+1)] = positions

    return inversionsDic



chord_type = "Minor"
key = "C"
octave = 3

the_chord = chord_with_inversions(chord_type, key, octave, chord_types)

voicings = chord_voicings["closed_4note"]

"""
for voicing in voicings:
    inversions = find_inversions_positions(the_chord, voicing)
    print("~~o"*20)
    print(inversions)
"""

def find_all_key_chords_with_inversions(chord_type, key):
    global chord_types
    voicings_name = chord_types[chord_type]['PossibleVoicings'][0]
    voicings = chord_voicings[voicings_name]
    
    all_notes_all_inversions = []
    list_of_the_note_positions = get_a_note_on_fterboard(key)
    set_of_objects = 1
    for i, pose in enumerate(list_of_the_note_positions):
        #print(pose)
        octave = int(pose["octave"])
        #print(chord_type,key,octave,voicings)
        the_chord = chord_with_inversions(chord_type, key, octave, chord_types)
        for voicing in voicings:
            inversions = find_inversions_positions(the_chord, voicing)
            all_notes_all_inversions.append(inversions)
            set_of_objects = set_of_objects + 1
    return all_notes_all_inversions

c = find_all_key_chords_with_inversions(chord_type, key)

print(c)