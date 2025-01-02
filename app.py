from flask import Flask, render_template, jsonify, request, url_for, session, redirect
from flask_cors import CORS
import zmq
import json
import numpy as np
import aubio
import math

from fretboard_coordinates import fretboard_coordinates
from fretboard_notes import fretboard_notes
from modes_pages import *
from modes_pages_r import *
from tenssions_pages import *
from fretboard_chord_types import get_chord_types, chord_types
from chord_on_fretboard import find_all_key_chords_with_inversions
from fretboard_inversions import generate_all_inversions
from fretboard_data_strcture import ChordCollection


import os
from dotenv import load_dotenv

# Load the .env file
load_dotenv()

app = Flask(__name__)
CORS(app)  # Allow all origins by default


chordCollection = ChordCollection()


# Initialize aubio pitch detector
sample_rate = 48000
pitch_detector = aubio.pitch("default", 4096, 4096, sample_rate)
pitch_detector.set_unit("Hz")
pitch_detector.set_silence(-40)

# Define the base notes for each string with their base frequency and octave
base_notes = [
    {"note": "E", "frequency": 82.41, "octave": 2},  # E2 (Low E string)
    {"note": "A", "frequency": 110.00, "octave": 2}, # A2
    {"note": "D", "frequency": 146.83, "octave": 3}, # D3
    {"note": "G", "frequency": 196.00, "octave": 3}, # G3
    {"note": "B", "frequency": 246.94, "octave": 3}, # B3
    {"note": "E", "frequency": 329.63, "octave": 4}  # E4 (High E string)
]

# Number of frets to consider
fret_count = 22

# Helper function to get the note name with octave based on frequency
def get_note_name(frequency):
    note_names = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
    # Calculate the MIDI note number
    note_index = round(12 * math.log2(frequency / 440.0)) + 69  # 440Hz is A4
    octave = (note_index // 12) - 1
    note = note_names[note_index % 12]
    return f"{note}{octave}"

# Generate all pitches for each string and fret
notes = []



for base_note in base_notes:
    for fret in range(fret_count + 1):
        frequency = base_note["frequency"] * (2 ** (fret / 12))
        note_name = get_note_name(frequency)
        notes.append({"note": note_name, "frequency": round(frequency, 2)})

#for note in notes:
#    print(note)

def get_closest_note(frequency):
    return min(notes, key=lambda note: abs(note["frequency"] - frequency)) if frequency > 0 else None

# Define the route for the home pagepython 
@app.route('/')
def home():
    return render_template('home.html')

# Define the route for the home pagepython 
@app.route('/fretboard')
def fretboard():
    return render_template('fretboard.html',
                           fretboard_coordinates = fretboard_coordinates,
                           fretboard_notes = fretboard_notes )

# Define the route for the home pagepython 
@app.route('/fretboard_active')
def fretboard_active():
    return render_template('fretboard_active.html',
                           fretboard_coordinates = fretboard_coordinates,
                           fretboard_notes = fretboard_notes )
# Define the route for the home pagepython 
@app.route('/learn_your_guitar_neck')
def learn_your_guitar_neck():
    return render_template('learn_your_guitar_neck.html',
                           fretboard_coordinates = fretboard_coordinates,
                           fretboard_notes = fretboard_notes )

@app.route('/learn_your_triads')
def learn_your_triads():
    return render_template(
        'fretboard_triads.html',
        fretboard_coordinates=fretboard_coordinates,
        fretboard_notes=fretboard_notes
    )

chords = get_chord_types()
#print(chords)
@app.route('/fretboard_chord_builder')
def fretboard_chord_builder():

    # Get all MP3 files from the static/audio directory
    audio_dir = os.path.join(app.static_folder, 'audio/single_notes')
    audio_files = [f for f in os.listdir(audio_dir) if f.endswith('.mp3')]
    print(audio_files)

    num_of_buttons_in_a_row = 4

    return render_template(
        'fretboard_chord_builder.html',
        fretboard_coordinates=fretboard_coordinates,
        fretboard_notes=fretboard_notes,
        chords = chords,
        num_of_buttons_in_a_row = num_of_buttons_in_a_row,
        audio_files=audio_files
    )

@app.route('/get_chord_list', methods=['GET'])
def get_chord_list():
    chords = chord_types

     # Check JSON validity
    try:
        json.dumps(chords)  # Serialize to JSON to ensure validity
        print("JSON is valid")
    except Exception as e:
        print(f"Invalid JSON: {e}")
        return jsonify({"error": "Invalid JSON"}), 500
    
    return jsonify(chords)

@app.route('/get_chord_data', methods=['GET'])
def get_chord_data():
    note = request.args.get('note')
    chord = request.args.get('chord')
    drop = request.args.get('drop')
    #print(request.args)

    chord = chord.replace("_", " ")
    print(chord,note)
    
    chordCollection.place_chord_on_fretboard(chord,note)
    chordCollection.rearrange_dictionary()
    cinfo = chordCollection.get_inversions_for_note_by_voicing()
     # Check JSON validity
    try:
        json.dumps(cinfo)  # Serialize to JSON to ensure validity
        print("JSON is valid")
    except Exception as e:
        print(f"Invalid JSON: {e}")
        return jsonify({"error": "Invalid JSON"}), 500
    
    return jsonify(cinfo)
'''
@app.route('/get_chord_data', methods=['GET'])
def get_chord_data():
    note = request.args.get('note')
    chord = request.args.get('chord')
    drop = request.args.get('drop')
    #print(request.args)

    chord = chord.replace("_", " ")

    #print(note,chord,drop)

    #c = find_all_key_chords_with_inversions(chord, note)
    
    cinfo = None
    if drop == "drop2":
        print("drop = ",drop)
        cinfo = generate_all_inversions(chord, note, True, False, False)
    elif drop == "drop3":
        print("drop = ",drop)
        cinfo = generate_all_inversions(chord, note, False, True, False)
    elif drop == "drop4":
        print("drop = ",drop)
        cinfo = generate_all_inversions(chord, note, False, False, True)
    else:
        print("drop = ",drop)
        cinfo = generate_all_inversions(chord, note, False, False, False)

     # Check JSON validity
    try:
        json.dumps(cinfo)  # Serialize to JSON to ensure validity
        print("JSON is valid")
    except Exception as e:
        print(f"Invalid JSON: {e}")
        return jsonify({"error": "Invalid JSON"}), 500
    
    return jsonify(cinfo)
'''

@app.route('/the_circle_of_fifths')
def the_circle_of_fifths():
    return render_template(
        'circle_of_fifths.html'
    )

@app.route('/circle_of_fifths_modes')
def circle_of_fifths_modes():
    return render_template('circle_of_fifths_modes.html', carousel_data=modes_carousel_data)

@app.route('/circle_of_fifths_tensions')
def circle_of_fifths_tensions():
    return render_template('circle_of_fifths_tensions.html', carousel_data=tenssions_carousel_data)

# Define the route for the home pagepython 
@app.route('/tuner')
def tuner():
    return render_template('tuner.html')

@app.route('/analyze-pitch', methods=['POST'])
def analyze_pitch():
    data = request.get_json()
    #audio_data = np.array(data['audioData'], dtype=np.float32).flatten()[:1024]
    audio_data = np.array(data['audioData'], dtype=np.float32)
    pitch = pitch_detector(audio_data)[0]

    # Get the closest note name
    note_name = get_closest_note(pitch)
    if pitch != 0 and note_name != None:
        print(pitch)
        print(get_closest_note(pitch))
    
    response = {"note": note_name, "pitch": float(pitch)}
    
    return jsonify(response)

from filter_data import filter_chord_data 
from fretboard_coordinates import fretboard_coordinates
@app.route('/filter', methods=['POST'])
def filter_data():
    # Get data from frontend request
    print("in filter")
    data = request.json
    note = data.get('note')
    inversion = data.get('inversion')
    chord_type = data.get('type')
    string_set = data.get('stringSet')
    note_interval = data.get('noteInterval')  # This can be 'intervals' or a specific note

    # Call filter function to get filtered chord data
    filtered_data = filter_chord_data(chord_type=chord_type, chord_key=note, inversion=inversion, string_set=string_set)

    # Prepare result list
    result = []
    for string_set_key, inversions in filtered_data.items():
        for inversion_name, notes_data in inversions:
            for string, note_data in notes_data.items():
                interval_name, fret, (note_letter, octave) = note_data[0], note_data[1], note_data[2]
                coordinate_key = (f'string_{string}', f'fret_{fret}')
                
                if coordinate_key in fretboard_coordinates:
                    x, y = fretboard_coordinates[coordinate_key]

                    if interval_name == 'root':
                        interval_name = 'R'
                    # Determine note name or interval
                    note_name = interval_name if note_interval == 'intervals' else note_letter

                    # Format pitch (e.g., "C#4")
                    pitch = f"{note_letter}{octave}"

                    # Add data to the result
                    result.append({
                        'id': f"{pitch}_{x}_{y}",  # ID format
                        'image': f"images/notes/note_{note_name}.png",  # Image path
                        'note': note_name,
                        'pitch': pitch,
                        'x': x,
                        'y': y,
                        'string': string,
                        'fret': fret,
                        'inversion': inversion_name,
                        'string_set': string_set_key
                    })

    #print(result)
    #print(len(result))
    # Return the result as JSON
    return jsonify(filtered_data=result)


'''
@app.route('/filter', methods=['POST'])
def filter_data():
    data = request.json
    note = data.get('note')
    inversion = data.get('inversion')
    type_ = data.get('type')
    string_set = data.get('stringSet')
    noteInterval = data.get('noteInterval')

    print("o~"*50)
    print("selected ----->>> ",note,inversion,type_,string_set,noteInterval)    

    #filter_chord_data(chord_type=type_, chord_key=note, inversion=inversion)
    filtered_data = filter_chord_data(chord_type=type_, chord_key=note, inversion=inversion, string_set=string_set)

    print(filtered_data)

    # Filtering logic - mock example
    #filtered_data = f"Filtered Data for {note}, {inversion}, {type_}, {string_set}"
    
    # Return as JSON to update frontend
    #return jsonify(filtered_data=filtered_data)
    return jsonify(filtered_data=filtered_data)
'''
if __name__ == '__main__':

    #app.run(debug=True)
    app.run(debug=True)

    
    