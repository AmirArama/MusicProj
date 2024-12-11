from fretboard_chord_types import chord_with_inversions, find_inversions_positions, chord_voicings, chord_types
from fretboard_map import get_note_data, get_root_note
from collections import defaultdict
from pprint import pprint


def process_nested_structure(data, group_order=None):
    """
    Process a nested dictionary structure to group and sort by specific keys.

    Args:
        data (dict): Nested dictionary with keys as string sets (e.g., '1_2_3_4') and values as lists of dictionaries.
        group_order (list, optional): List of keys defining the desired order within each group.
                                      If None, the order is determined by the keys in the data.

    Returns:
        dict: Processed nested dictionary with grouped and sorted data.
    """
    result = {}

    for string_set, items in data.items():
        # Group dictionaries within the current string set by their keys
        grouped_data = defaultdict(list)
        for item in items:
            if isinstance(item, dict):  # Ensure item is a dictionary
                for key, value in item.items():
                    grouped_data[key].append(value)  # Group by 'root', 'inversion1', etc.
            else:
                print(f"Skipping non-dictionary item in group '{string_set}': {item}")

        # Sort grouped data based on group_order
        sorted_group = []
        if group_order:
            for key in group_order:
                if key in grouped_data:
                    sorted_group.append({key: grouped_data[key]})
        else:
            # Use the natural order of keys in grouped_data if no group_order is provided
            for key, value in grouped_data.items():
                sorted_group.append({key: value})

        # Add the processed data back to the result under the string set
        result[string_set] = sorted_group

    res = {}
    for i in result.keys():
        for key, value in data.items():
            #print("~o"*30)        

            #pprint(key)
            invDic = {}
            for r in value:
                for key2, val2 in r.items():
                    if key2 not in invDic:
                        invDic[key2] = [val2]
                    else:
                        invDic[key2].append(val2)
            res[key] = invDic
       
    #pprint(res)
    return res



def generate_all_inversions(chord_name,key):

    chord_info = chord_types[chord_name]
    voicings_name = chord_info['PossibleVoicings'][0]
    voicings = chord_voicings[voicings_name]
    #print(chord_info)

    y = chord_with_inversions(chord_name, key, 3, chord_types)
    #print(y)


    keys = get_root_note(key)
    #print(keys)
    listOfPitch = []
    for key_ in keys:
        if key_[1][-1] not in listOfPitch: 
            listOfPitch.append(key_[1][-1])
    print(listOfPitch) 

    availableChords = {}
    for pitch in listOfPitch:
        availableChords[key+pitch] = chord_with_inversions(chord_name, key, pitch, chord_types)

    finalInversionMap = {}
    for voicing in voicings:
        print(voicing)
        InvList = []
        for chord in availableChords.values():
            x = find_inversions_positions(chord, voicing)
            if x != None:
                print(x)
                InvList.append(x)
        k = "_".join(map(str, voicing))
        print(k)
        finalInversionMap[k] = InvList
        #print(voicing)

    return process_nested_structure(finalInversionMap)

x = generate_all_inversions("Major",'C')

#from pprint import pprint
#pprint(x)

