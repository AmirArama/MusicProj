from flask import Flask, render_template, jsonify, request, url_for, session, redirect
import zmq
import json
import numpy as np
import aubio
import math

from fretboard_coordinates import fretboard_coordinates
from fretboard_notes import fretboard_notes
from modes_pages import *



import os
from dotenv import load_dotenv

# Load the .env file
load_dotenv()

app = Flask(__name__)

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

@app.route('/the_circle_of_fifths')
def the_circle_of_fifths():
    return render_template(
        'circle_of_fifths.html'
    )

@app.route('/circle_of_fifths_modes')
def circle_of_fifths_modes():
    carousel_data = [
        {
            "title": "My Journey to Simplify Music Theory",
            "content": page1 ,
            "page_number": 1
        },
        {
            "title": "Modes",
            "content": page2,
            "page_number": 2
        },
        {
            "title": "Modes",
            "content": page3,
            "page_number": 3,
        },
        {
            "title": "Modes",
            "content": page4,
            "page_number": 4,
            "image": page4Image,
            "image_size": page4imageSize
        },
        {
            "title": "Modes",
            "content": page5,
            "page_number": 5,
            "image": page5Image,
            "image_size": page5imageSize
        },
        {
            "title": "Modes",
            "content": page6,
            "page_number": 6,
            "image": page6Image,
            "image_size": page6imageSize
        },
        {
            "title": "Modes",
            "content": page7,
            "page_number": 7,
        },
        {
            "title": "Modes",
            "content": page8,
            "page_number": 8,
        },
        {
            "title": "Modes",
            "content": page9,
            "page_number": 9,
        },
        {
            "title": "Modes",
            "content": page10,
            "page_number": 10,
            "image": page10Image,
            "image_size": page10imageSize
        },
        {
            "title": "Modes",
            "content": page11,
            "page_number": 11,
            "image": page10Image,
            "image_size": page10imageSize
        },
        {
            "title": "Modes",
            "content": page12,
            "page_number": 12,
        },
        {
            "title": "Modes",
            "content": page13,
            "page_number": 13,
        },
        {
            "title": "Modes",
            "content": page14,
            "page_number": 14,
        },
        {
            "title": "Modes",
            "content": page15,
            "page_number": 15,
        },
        {
            "title": "Modes",
            "content": page16,
            "page_number": 16,
        }
    ]
    return render_template('circle_of_fifths_modes.html', carousel_data=carousel_data)

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

    print(result)
    print(len(result))
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
    