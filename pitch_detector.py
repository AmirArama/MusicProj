import librosa
import numpy as np

# Load the audio file
audio_path = 'note_files/clean-guitar-note_A_minor.wav'
y, sr = librosa.load(audio_path, sr=None)

# Estimate fundamental frequency using YIN algorithm
f0, voiced_flag, voiced_probs = librosa.pyin(y, fmin=50, fmax=1000, sr=sr)

# Extract the average fundamental frequency ignoring unvoiced parts
f0_mean = np.nanmean(f0)
print(f"The estimated fundamental frequency is: {f0_mean:.2f} Hz")
