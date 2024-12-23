from fretboard_chord_types import chord_types, interval_to_semitones , chord_voicings, get_note_data, interval_to_name
from fretboard_map import fretboard_data_sharp, fretboard_data_flat
from collections import defaultdict


voicings = {
    'closed_triad': [
        [(0,0),(1,0),(2,0)],
        [(1,0),(2,0),(0,1)],
        [(2,0),(0,1),(1,1)],
    ],
    "closed_4note": [
        [(0, 0), (1, 0), (2, 0), (3, 0)],
        [(1, 0), (2, 0), (3, 0), (0, 1)],
        [(2, 0), (3, 0), (0, 1), (1, 1)],
        [(3, 0), (0, 1), (1, 1), (2, 1)]
    ],
    "drop_2": [
        [(2,-1), (0, 0), (1, 0), (3, 0)],
        [(3,-1), (1, 0), (2, 0), (0, 1)],
        [(0, 0), (2, 0), (3, 0), (1, 1)],
        [(1, 0), (3, 0), (0, 1), (2, 1)]
    ],
    "drop_3": [
        [(1,-1), (0, 0), (2, 0), (3, 0)],
        [(2,-1), (1, 0), (3, 0), (0, 1)],
        [(3,-1), (2, 0), (0, 1), (1, 1)],
        [(0, 0), (3, 0), (1, 1), (2, 1)]
    ],
    "drop_2_and_4": [
        [(0,-1), (2,-1), (1, 0), (3, 0)],
        [(1,-1), (3,-1), (2, 0), (0, 1)],
        [(2,-1), (0, 0), (3, 0), (1, 1)],
        [(3,-1), (1, 0), (0, 1), (2, 1)]
    ],
    "drop_2_and_3": [
        [(1,-1), (2,-1), (0, 0), (3, 0)],
        [(2,-1), (3,-1), (1, 0), (0, 1)],
        [(3,-1), (0, 0), (2, 0), (1, 1)],
        [(0, 0), (1, 0), (3, 0), (2, 1)]
    ]
}

class ChordClass:

    def __init__(self, chordName):
        self.chordName = chordName
        self.FullChordName = None
        self.FullChordNotes = None
        self.key = None
        self.symbols = None
        self.stracture = None
        self.inversionsNotes = None
        self.inversionsIntervals = None
        self.inversionsNames = None
        self.voicings = None
        self.inversionsOnStrings = None
        self.inversionsForNoteByVoicing = None
        

        self.chromatic_notes_flat = ["C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab", "A", "Bb", "B"]
        self.chromatic_notes_sharp = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]

        self.loadData(chord_types)
        self.builldInversionsIntervals()
        
    def loadData(self,chorsdData):        
        chordData = chorsdData[self.chordName]
        self.symbols = chordData['Symbols']
        self.stracture = chordData['Function']
        self.voicings = chordData['PossibleVoicings']

    def builldInversionsIntervals(self):
        inversions = {}
        for voice in self.voicings:
            inversions[voice] = []
            for idx,inversion in enumerate(voicings[voice]):
                inv = [0]*len(inversion)
                for idx2, note in enumerate(inversion):
                    inv[idx2] = self.stracture[note[0]] 
                inversions[voice].append(inv)
        self.inversionsIntervals = inversions
    
    def builldInversionsNotes(self):
        if self.FullChordNotes == None:
            print("\nError: No available chord notes")
            print("Error: Please call the build_chord function first\n")
            pass

        theNotes = self.FullChordNotes
        self.inversionsNotes = {}
        for voice in self.inversionsIntervals.keys():
            inversionsStracture = voicings[voice]
            self.inversionsNotes[voice] = []
            for inv in inversionsStracture:
                noteList = []
                for invElemet in inv:
                    idx = invElemet[0]
                    octaveShift = invElemet[1]

                    key = theNotes[idx][:-1]
                    octave = int(theNotes[idx][-1])+octaveShift

                    noteList.append(key + str(octave))
                self.inversionsNotes[voice].append(noteList)

    def build_chord(self,key_with_pitch):
       
        key = key_with_pitch[:-1]
        octave = int(key_with_pitch[-1])
        chord_data = self.stracture

        # Determine the appropriate chromatic scale based on the root note
        if key in self.chromatic_notes_flat:
            scale = self.chromatic_notes_flat
        elif key in self.chromatic_notes_sharp:
            scale = self.chromatic_notes_sharp
        else:
            return {"error": f"Root note '{key}' is not valid."}

        # Find the root index in the chromatic scale
        root_index = scale.index(key)

        # Build the chord notes with pitch
        chord_notes_with_pitch = [f"{key}{octave}"]
        current_octave = octave

        for interval in chord_data:
            if interval == "1":
                continue

            # Map the interval to semitones
            semitones = interval_to_semitones[interval]["semitones"]
            # Calculate the note index in the chromatic scale
            note_index = (root_index + semitones) % 12
            # Determine the octave shift
            octave_shift = (root_index + semitones) // 12
            current_octave += octave_shift

            # Append the note with pitch
            chord_notes_with_pitch.append(f"{scale[note_index]}{current_octave}")

        # Determine the chord name using the first symbol
        chord_symbol = self.symbols[0]
        self.FullChordName = f"{key}{chord_symbol}"
        self.FullChordNotes = chord_notes_with_pitch

    def findinversion_on_fretboard(self):

        '''
            Reverse the inversions to make the root position on the bass.
            Both for Intervals and Notes
        '''
        self.reversed_inversionsNotes = {}
        for voicong,inversions in self.inversionsNotes.items():
            self.reversed_inversionsNotes[voicong] = []
            for inversion in inversions:
                # Reverse the inversions to make the root position on the bass.
                self.reversed_inversionsNotes[voicong].append(inversion[::-1])

        self.reversed_inversionsIntervals = {}
        for voicong,inversions in self.inversionsIntervals.items():
            self.reversed_inversionsIntervals[voicong] = []
            for inversion in inversions:
                self.reversed_inversionsIntervals[voicong].append(inversion[::-1])     

        '''
            Now lets place it on the strings voicing 
        '''
        notesOnFretboard = {}
        for voice, inversions in self.reversed_inversionsNotes.items():
            #print(voice, inversions)
            #print(voice, self.reversed_inversionsIntervals[voice])
            #print(chord_voicings[voice])

            string_sets = chord_voicings[voice]
            inversionsIntervals = self.reversed_inversionsIntervals[voice]
            notesOnFretboard[voice] = {}
            for string_set in string_sets:
                string_set_str= "_".join(map(str, string_set))
                notesOnFretboard[voice][string_set_str] = {}
                #print("\nstringset =", string_set_str)
                for idx, inversion in enumerate(inversions):
                    inversionIntervals = inversionsIntervals[idx]
                    #print("\n" + "-" * 60)
                    #print("voicing = ", voice, ", InveersionNote = ", inversion)
                    #print("voicing = ", voice, ", InveersionIntervals = ", inversionIntervals)
                    #print("-" * 60)

                    inversion_on_fretboard = []
                    string_on_fretboard = []
                    inversionf = True
                    for idx2, (string, note) in enumerate(zip(string_set, inversion)):
                        note_on_fretboard = get_note_data(string - 1, note)
                        if note_on_fretboard is None:
                            inversionf = False
                        else:
                            inversion_on_fretboard.append(note_on_fretboard)

                            if "flat" in note_on_fretboard["jsnote"]:
                                note_on_fretboard["note_sound"] = "string" + str(string) + "_" + note[0]+note[2] + "_flat"
                            elif "sharp" in note_on_fretboard["jsnote"]:
                                note_on_fretboard["note_sound"] = "string" + str(string) + "_" + note[0]+note[2] + "_sharp"
                            else:
                                note_on_fretboard["note_sound"] = "string" + str(string) + "_" + note

                            intervl = inversionIntervals[idx2]
                            note_on_fretboard["interval"] = intervl
                            note_on_fretboard["jsinterval"] = interval_to_name[intervl]

                            string_on_fretboard.append(string)
                    if inversionf:
                        #print(inversion_on_fretboard)
                        inversion_name = self.get_inversion_name(inversion_on_fretboard)
                        notesOnFretboard[voice][string_set_str][inversion_name] = inversion_on_fretboard
                    else:
                        pass
                        #print("Can't place inversion")
            self.inversionsOnStrings = notesOnFretboard
            #print("Final notes on fretboard", notesOnFretboard)

    def get_inverssions(self):
        return self.inversionsOnStrings

    def find_note_index(self,note):
        if note in self.chromatic_notes_flat:
            return self.chromatic_notes_flat.index(note)
        elif note in self.chromatic_notes_sharp:
            return self.chromatic_notes_sharp.index(note)
        else:
            return -1

    def set_note(self,note):
        self.build_chord(note)
        self.builldInversionsNotes()
        self.findinversion_on_fretboard()
    
    def get_inversion_name(self,inversion_dict):

        first_note = inversion_dict[0]['note'][0]
        original_chord = self.FullChordNotes
        original_chord = original_chord[::-1]

        chord_len = len(original_chord)
        if chord_len == 3:
            if first_note == original_chord[0][0]:
                return "root"
            elif first_note == original_chord[chord_len-1][0]:
                return "inversion1"
            elif first_note == original_chord[chord_len-2][0]:
                return "inversion2"
            else:
                print(first_note,original_chord)
                return "Unknown inversion"
        elif chord_len == 4:
            if first_note == original_chord[0][0]:
                return "root"
            elif first_note == original_chord[chord_len-1][0]:
                return "inversion1"
            elif first_note == original_chord[chord_len-2][0]:
                return "inversion2"
            elif first_note == original_chord[chord_len-3][0]:
                return "inversion3"
            else:
                return "Unknown inversion"
        else:
            return "Invalid chord length"
        
    def __str__(self):
        dataForPring = "\n"+"-"*40+"\n"
        dataForPring += f"Data for a {self.chordName} chord\n"
        dataForPring += "-"*40+"\n\n"
        dataForPring += f"Possible Symbols: {self.symbols}\n"
        dataForPring += f"Chord stracture {self.stracture}\n"
        dataForPring += f"Applicable voicings {self.voicings}\n"
        dataForPring += "\n\n"
        dataForPring += "Inversions Intervals:\n"
        dataForPring += "~~"*60+"\n"
        for key,value in self.inversionsIntervals.items():
            dataForPring += f"{key}: {value}\n"
        dataForPring += "~~"*60+"\n\n"

        dataForPring += f"Object set to {self.FullChordName} chord:\n"
        dataForPring += "-"*40+"\n"
        dataForPring += f"Chord notes are: {self.FullChordNotes}\n"

        dataForPring += "\n\n"
        dataForPring += "Notes Intervals:\n"
        dataForPring += "~~"*60+"\n"
        if self.inversionsNotes != None:
            for key,value in self.inversionsNotes.items():
                dataForPring += f"{key}: {value}\n"
            dataForPring += "~~"*60+"\n\n"

            original_chord = self.FullChordNotes
            original_chord = original_chord[::-1]
            for voice,stringsets in self.inversionsOnStrings.items():

                dataForPring += f"Voicing = {voice}\n"
                dataForPring += "~~"*60+"\n"
                for stringset,inversion in stringsets.items():
                    dataForPring += f"Set = {stringset} , {original_chord}\n"
                    dataForPring += "--"*60+"\n"
                    for key,value in inversion.items():
                        dataForPring += f"{key}: {value}\n\n"

        return dataForPring


# Example of using the class
#chord = ChordClass("Diminished seventh")
#chord.set_note("C4")
#print(chord)  # Calls the __str__ method


class ChordCollection:
    def __init__(self):
        self.chordTypes = chord_types.keys()
        self.inversionsForNote = None
        self.chords = {}

        self.populate_chords()

    def add_chord(self, chord_name):
        self.chords[chord_name] = ChordClass(chord_name)

    def populate_chords(self):
        chord_names = self.chordTypes
        for chord_name in chord_names:
            self.add_chord(chord_name)

    def set_notes_for_chord(self, chord_name, notes):
        if chord_name in self.chords:
            self.chords[chord_name].set_notes(notes)

    def get_chord(self, chord_name):
        return self.chords.get(chord_name)
    
    def set_note(self,note):
        fdata = fretboard_data_flat
        if len(note) > 1 and note[1] == "#":
            fdata = fretboard_data_sharp
            xlist = [key for key in fdata.keys() if key[1].startswith(note) and (len(key[1]) == 3)]
        elif len(note) > 1 and note[1] == "b":
            fdata = fretboard_data_flat
            xlist = [key for key in fdata.keys() if key[1].startswith(note) and (len(key[1]) == 3)]
        else:
            fdata = fretboard_data_flat
            xlist = [key for key in fdata.keys() if key[1].startswith(note) and (len(key[1]) == 2)]   
        
        notes_list = []
        for val in xlist:
            if val[1] not in notes_list:
                notes_list.append(val[1])
        return notes_list
    
    def place_chord_on_fretboard(self,chordName,note):
        root_notes = self.set_note(note) 
        chord = self.get_chord(chordName)
        finalDict = {}
        for note in root_notes:
            chord.set_note(note)
            #print(f"\nrunning on note {note}")
            #print("-"*60)
            ldata = chord.get_inverssions()
            finalDict[note] = {}
            for voice, inversion in ldata.items():
                #print(f"\nrunning on voicing {voice}")
                #print("~"*60)
                finalDict[note][voice] = {}
                for string,inversion in inversion.items():
                    finalDict[note][voice][string]=inversion
                    #print(f"\nrunning on voicing {string}")
                    #print("+"*60)
                    #if not inversion:
                        #print(f"Inversion not found!")
                    #else:
                        #print(f"Inversions {inversion}")
        self.inversionsForNote = finalDict

    def get_inversions_for_note(self):
        return self.inversionsForNote

    def rearrange_dictionary(self):
        massive_dict = self.inversionsForNote
        # Initialize the new structure
        rearranged_dict = defaultdict(lambda: defaultdict(lambda: defaultdict(list)))

        # Iterate over each pitch and its data
        for pitch, pitch_data in massive_dict.items():
            for voicing, voicing_data in pitch_data.items():
                for string_set, string_set_data in voicing_data.items():
                    for inversion, inversion_data in string_set_data.items():
                        # Append the inversion data as a list
                        rearranged_dict[voicing][string_set][inversion].append(inversion_data)

        self.inversionsForNoteByVoicing = rearranged_dict
        # Convert to a regular dictionary for compatibility

    def get_inversions_for_note_by_voicing(self,voice = "all"):
        if voice == "all":
            return self.inversionsForNoteByVoicing
        else:
            if voice in self.inversionsForNoteByVoicing:
                return self.inversionsForNoteByVoicing[voice]
            else:
                return {"Voice":"Does Not Exist"}
    
    def __str__(self):
        dataForPring = "\nThe Chord collection is:\n"
        dataForPring += "-"*80+"\n"
        for key,value in self.chords.items():
            dataForPring += f"{key}, "
        dataForPring += "\n"+"-"*80+"\n\n"
        return dataForPring
'''
chordCollection = ChordCollection()
print(chordCollection) 
chordCollection.place_chord_on_fretboard("Diminished seventh","E")
x = chordCollection.get_inversions_for_note()
#print(x)
# Example usage:
chordCollection.rearrange_dictionary()
rearranged = chordCollection.get_inversions_for_note_by_voicing("closed_4note")

# You can print or save the rearranged data to verify the structure
import json
print(json.dumps(rearranged, indent=2))
#chord = chordCollection.get_chord("Diminished")
#chord.set_note("E3")
#x = chord.get_inverssions()
#print(chordCollection.set_note("F#"))
'''