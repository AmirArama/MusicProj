from pydub import AudioSegment

# Constants
bpm = 120
time_signature = 4  # 4/4
seconds_per_beat = 60 / bpm
measure_duration = seconds_per_beat * time_signature  # Duration of one measure (in seconds)
measure_duration_ms = measure_duration * 1000  # Convert to milliseconds
num_frets = 22  # Total frets to process

# Note names for each string up to the 22nd fret
note_names_by_string = [
    ["E4", "F4", "F#4", "G4", "G#4", "A4", "A#4", "B4", "C5", "C#5",
     "D5", "D#5", "E5", "F5", "F#5", "G5", "G#5", "A5", "A#5", "B5", "C6", "C#6"],  # String 1
    ["B3", "C4", "C#4", "D4", "D#4", "E4", "F4", "F#4", "G4", "G#4",
     "A4", "A#4", "B4", "C5", "C#5", "D5", "D#5", "E5", "F5", "F#5", "G5", "G#5"],  # String 2
    ["G3", "G#3", "A3", "A#3", "B3", "C4", "C#4", "D4", "D#4", "E4",
     "F4", "F#4", "G4", "G#4", "A4", "A#4", "B4", "C5", "C#5", "D5", "D#5", "E5"],  # String 3
    ["D3", "D#3", "E3", "F3", "F#3", "G3", "G#3", "A3", "A#3", "B3",
     "C4", "C#4", "D4", "D#4", "E4", "F4", "F#4", "G4", "G#4", "A4", "A#4", "B4"],  # String 4
    ["A2", "A#2", "B2", "C3", "C#3", "D3", "D#3", "E3", "F3", "F#3",
     "G3", "G#3", "A3", "A#3", "B3", "C4", "C#4", "D4", "D#4", "E4", "F4", "F#4"],  # String 5
    ["E2", "F2", "F#2", "G2", "G#2", "A2", "A#2", "B2", "C3", "C#3",
     "D3", "D#3", "E3", "F3", "F#3", "G3", "G#3", "A3", "A#3", "B3", "C4", "C#4"],  # String 6
]

# Process each string file
for string_num in range(1, 7):  # Strings 1 to 6
    # Load the WAV file for the current string
    audio_path = f"note_files/strings/string{string_num}.wav"
    print(f"Processing {audio_path}...")
    try:
        audio = AudioSegment.from_file(audio_path)
    except Exception as e:
        print(f"Error loading {audio_path}: {e}")
        continue

    # Get the note names for the current string
    note_names = note_names_by_string[string_num - 1]

    # Split and export each note
    for fret_num in range(num_frets):  # 0 to 21 (total 22 frets)
        start_time = fret_num * measure_duration_ms
        end_time = start_time + measure_duration_ms
        note_audio = audio[start_time:end_time]
        note_name = note_names[fret_num]  # Get the corresponding note name
        output_filename = f"string{string_num}_{note_name}.wav"
        note_audio.export(output_filename, format="wav")
        print(f"Exported: {output_filename}")


print("All strings and notes have been processed successfully!")
