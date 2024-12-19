import librosa
import soundfile as sf
import sounddevice as sd

# Step 1: Load the original sample
audio_path = 'note_files/clean-guitar-note_A_minor.wav'  # Replace with your file path
y, sr = librosa.load(audio_path, sr=None)  # Preserve original sample rate

# Step 2: Calculate semitone shift (110 Hz to 440 Hz is 2 octaves up)
semitone_shift = 12 * 2  # 12 semitones per octave × 2 octaves = 24 semitones

# Step 3: Shift the pitch
transposed_audio = librosa.effects.pitch_shift(y, sr=sr, n_steps=semitone_shift)

# Step 4: Save the transposed audio to a new file
output_path = 'guitar_110_to_440_pitch_shifted.wav'
sf.write(output_path, transposed_audio, sr)

# Step 5: Play the transposed audio
print(f"Transposed audio saved as {output_path}")
sd.play(transposed_audio, sr)
sd.wait()
