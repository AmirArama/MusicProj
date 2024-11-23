import json
#file1 = 'two_level_dict.json'
file1 = 'two_level_dict_new.json'

with open(file1, "r") as file:
    data = json.load(file)
#print(data)

def filter_chord_data(chord_data=data, chord_type=None, chord_key=None, inversion=None, string_set=None):
    """
    Filters the chord data based on type, key, inversion, and string set.
    
    Parameters:
    - chord_data (dict): The dictionary containing all chord information.
    - chord_type (str): The type of chord to filter by (e.g., 'augmented', 'major', 'minor').
    - chord_key (str): The root key of the chord to filter by (e.g., 'C', 'D', etc.).
    - inversion (str): The inversion to filter by ('root', '1st_inversion', '2nd_inversion'). 
                       Use None to get all inversions.
    - string_set (str): The string set to filter by ('123', '234', '345', '456').
                        Use None to get all string sets.

    Returns:
    - dict: Filtered dictionary based on the provided criteria.
    """
    # Normalize 'all' to None for filtering purposes
    if inversion == 'all':
        inversion = None
    if string_set == 'all':
        string_set = None
    if "#" in chord_key:
            chord_key = chord_key.replace("#", "_sharp")

    print("Filtering by:", chord_type, chord_key, inversion, string_set)
    # Start with the full dictionary
    filtered_data = chord_data

    # Filter by chord type if provided
    if chord_type:
        filtered_data = filtered_data.get(chord_type, {})

    # Filter by chord key if provided
    if chord_key:
        filtered_data = filtered_data.get(chord_key, {})

    # Filter by string set if provided
    if string_set:
        filtered_data = {string_set: filtered_data.get(string_set, [])}
    
    # Filter by inversion if provided
    if inversion:
        filtered_data = {
            s_set: [
                [inv, notes]
                for inv, notes in inversions
                if inv == inversion
            ]
            for s_set, inversions in filtered_data.items()
        }
    
    # Remove empty entries after filtering by inversion or string set
    filtered_data = {k: v for k, v in filtered_data.items() if v}
    
    return filtered_data



# Filter by type, key, and inversion
#filtered = filter_chord_data(data, chord_type="augmented", chord_key="C", inversion="1st_inversion")
#print(filtered)

filtered = filter_chord_data(data, chord_type="augmented", chord_key="D")
print(filtered)
