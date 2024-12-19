from pydub import AudioSegment

# Load the WAV file
audio_path = "note_files/string1.wav"  # Replace with your file name
audio = AudioSegment.from_file(audio_path)

# Constants
bpm = 120
time_signature = 4  # 4/4
seconds_per_beat = 60 / bpm
measure_duration = seconds_per_beat * time_signature  # Duration of one measure (in seconds)
measure_duration_ms = measure_duration * 1000  # Convert to milliseconds
num_notes = 22  # Total notes in the audio

# Define note names for the E string up to the 22nd fret
note_names = [
    "E4", "F4", "F#4", "G4", "G#4", "A4", "A#4", "B4", "C5", "C#5",
    "D5", "D#5", "E5", "F5", "F#5", "G5", "G#5", "A5", "A#5", "B5", "C6", "C#6"
]

# Split and export each note
for i in range(num_notes):
    start_time = i * measure_duration_ms
    end_time = start_time + measure_duration_ms
    note_audio = audio[start_time:end_time]
    note_name = note_names[i]  # Get the corresponding note name
    output_filename = f"{note_name}.wav"
    note_audio.export(output_filename, format="wav")
    print(f"Exported: {output_filename}")

print("All notes have been exported successfully!")
