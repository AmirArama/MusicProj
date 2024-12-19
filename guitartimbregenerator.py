import numpy as np
import sounddevice as sd

def generate_string_tone(frequency, duration, harmonics, sr=44100):
    t = np.linspace(0, duration, int(sr * duration), endpoint=False)
    signal = np.zeros_like(t)
    for i, amp in enumerate(harmonics):
        signal += amp * np.sin(2 * np.pi * frequency * (i + 1) * t)
    signal /= np.max(np.abs(signal))  # Normalize the amplitude
    return signal

harmonics = [1, 0.5, 0.3, 0.2, 0.1]  # Amplitudes of harmonics
tone = generate_string_tone(440, 2, harmonics)  # A4, 2 seconds
sd.play(tone)
sd.wait()
