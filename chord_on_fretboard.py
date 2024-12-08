from collections import defaultdict
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
            #if string_set == [4,5,6]:
                #print(note_pitch)

            if "b" in note_name:
                frets = [(fret,note_name+str(note_pitch)) for fret, n in enumerate(notes_22frets_flat['string'+str(string_)]) if n[0] == note_name and n[1] == str(note_pitch)]
            else:
                frets = [(fret,note_name+str(note_pitch)) for fret, n in enumerate(notes_22frets_sharp['string'+str(string_)]) if n[0] == note_name and n[1] == str(note_pitch)]
           
            if not frets:
                found_position = False
            else:
                #if string_set == [4,5,6]:
                #    print(notes_22frets_flat)
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



chord_type = "Major"
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
    unique_items = set()

    list_of_the_note_positions = get_a_note_on_fterboard(key)
    print(list_of_the_note_positions)
    set_of_objects = 1
    num_of_inversions = 0
    for i, pose in enumerate(list_of_the_note_positions):
        #print(pose)
        octave = int(pose["octave"])
        #print(chord_type,key,octave,voicings)
        the_chord = chord_with_inversions(chord_type, key, octave, chord_types)
        for voicing in voicings:
            """
            if pose["string"] in voicing:
                #print(voicing,pose)
                #print(voicing,"add")
                pass
            else:
                #print("skip")
                continue
            """
            inversions = find_inversions_positions(the_chord, voicing)
            if inversions["fb_inversion_1"] == "None" and inversions["fb_inversion_2"] == "None" and inversions["fb_inversion_3"] == "None":
                continue 
            data = make_immutable(inversions)
            if data not in unique_items:
                unique_items.add(data)
                #print("Added to unique items")
                all_notes_all_inversions.append(inversions)        
            #else:
                #print("Duplicate found!")   
            #if inversions["fb_inversion_1"] != "None":
            #    num_of_inversions += 1
            
            #print("~o"*30)
            #print(inversions)
            #print("~o"*30)
            set_of_objects = set_of_objects + 1
    #print("inv num = ",num_of_inversions)
    all_notes_all_inversions2 = {} 
    for voicing in voicings:

        string_key = "".join(map(str, voicing))  # Convert each element to a string and join with "_"
        x = all_notes_all_inversions2[string_key] = {}
        x['root'] = []
        x['1stInversion'] = []
        x['2ndInvrsion'] = []
        x['3rdInversion'] = []
        for idx,val in enumerate(all_notes_all_inversions):
            if val['string set'] == voicing: 
                for idx2 in range(5):
                    iver = "fb_inversion_"+str(idx2)
                    if iver in val:
                        if val[iver] != "None":
                            if idx2 == 1:
                                x['root'].append(val[iver])  
                            elif idx2 == 2:
                                x['1stInversion'].append(val[iver])
                            elif idx2 == 3:
                                x['2ndInvrsion'].append(val[iver])
                            elif idx2 == 4:
                                x['3rdInversion'].append(val[iver])


    

    return all_notes_all_inversions2

c = find_all_key_chords_with_inversions(chord_type, key)

from pprint import pprint
#pprint(c)
    
def find_all_key_chords_with_inversions_immutable(chord_type, key):
    data = find_all_key_chords_with_inversions(chord_type, key)
    return make_immutable(data)

#c = find_all_key_chords_with_inversions_immutable(chord_type, key)
from pprint import pprint

#pprint(c)
#print(c)