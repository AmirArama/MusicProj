from fretboard_chord_types import chord_types, interval_to_semitones , chord_voicings, get_note_data, interval_to_name

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
        for voice,inversions in self.reversed_inversionsNotes.items():
            print(voice,inversions)
            print(voice,self.reversed_inversionsIntervals[voice])
            print(chord_voicings[voice])

            string_sets = chord_voicings[voice]
            inversionf = True
            inversionsIntervals = self.reversed_inversionsIntervals[voice]

            for idx, inversion in enumerate(inversions):
                inversionIntervals = inversionsIntervals[idx]
                print("\n"+"-"*60)
                print("voicing = ", voice, ", InveersionNote = " ,inversion)
                print("voicing = ", voice, ", InveersionIntervals = " ,inversionIntervals)
                print("-"*60)
                for string_set in string_sets:
                    print("\nstringset =", string_set)                        
                    
                    inversion_on_fretboard = []
                    string_on_fretboard = []
                    for idx2, (string , note) in enumerate(zip(string_set,inversion)):
                        note_on_fretboard = get_note_data(string-1,note)
                        if note_on_fretboard == None:
                            inversionf = False
                        else:
                            inversion_on_fretboard.append(note_on_fretboard)

                            if "flat" in note_on_fretboard["jsnote"]:
                                note_on_fretboard["note_sound"] = "string"+str(string)+"_"+note[0]+"_flat"
                            elif "sharp" in note_on_fretboard["jsnote"]:
                                note_on_fretboard["note_sound"] = "string"+str(string)+"_"+note[0]+"_sharp"

                            intervl = inversionIntervals[idx2]    
                            note_on_fretboard["interval"] = intervl    
                            note_on_fretboard["jsinterval"] = interval_to_name[intervl]

                            string_on_fretboard.append(string)
                    if inversionf == True:
                        print(inversion_on_fretboard)
                    else:
                        print("Can't place inversion")

    def find_note_index(self,note):
        if note in self.chromatic_notes_flat:
            return self.chromatic_notes_flat.index(note)
        elif note in self.chromatic_notes_sharp:
            return self.chromatic_notes_sharp.index(note)
        else:
            return -1
        
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
        for key,value in self.inversionsNotes.items():
            dataForPring += f"{key}: {value}\n"
        dataForPring += "~~"*60+"\n\n"


        return dataForPring


# Example of using the class
chord = ChordClass("Diminished seventh")
chord.build_chord("C4")
chord.builldInversionsNotes()
chord.findinversion_on_fretboard()
#chord = ChordClass("Diminished")

print(chord)  # Calls the __str__ method
