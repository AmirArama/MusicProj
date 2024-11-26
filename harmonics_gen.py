import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq

# Fundamental frequency for C3
fundamental_freq = 130.81  # Hz

# Sampling parameters
sampling_rate = 44100  # Samples per second
duration = 0.05        # Duration in seconds for each waveform

# Time array
t = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False)

# Number of harmonics to display
num_harmonics = 8

# Corresponding note names for the first eight harmonics
note_names = ['C3', 'C4', 'G4', 'C5', 'E5', 'G5', 'A♯5', 'C6']

# Colors for each harmonic
colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'orange']

# Initialize the composite waveform
composite_waveform = np.zeros_like(t)

# Create subplots for time-domain waveforms
fig, axes = plt.subplots(num_harmonics, 1, figsize=(10, 12), sharex=True)

for n in range(1, num_harmonics + 1):
    # Frequency of the nth harmonic
    freq = fundamental_freq * n
    # Amplitude scaling factor (1/n)
    amplitude = 1 / n
    # Generate the waveform for the nth harmonic
    waveform = amplitude * np.sin(2 * np.pi * freq * t)
    # Add to the composite waveform
    composite_waveform += waveform
    # Plot the waveform
    axes[n - 1].plot(t, waveform, color=colors[n - 1], linewidth=2)
    axes[n - 1].set_title(f'Harmonic {n}: {note_names[n - 1]} ({freq:.2f} Hz)')
    axes[n - 1].set_ylabel('Amplitude')
    axes[n - 1].grid(True)

# Set the x-axis label for the last subplot
axes[-1].set_xlabel('Time (seconds)')

# Adjust layout
plt.tight_layout()
plt.savefig('harmonic_waveforms_attenuated.png')
plt.show()

# Compute the Fourier Transform of the composite waveform
N = len(t)
yf = fft(composite_waveform)
xf = fftfreq(N, 1 / sampling_rate)[:N // 2]

# Plot the frequency spectrum
plt.figure(figsize=(10, 6))
plt.plot(xf, 2.0 / N * np.abs(yf[:N // 2]), 'b')
plt.title('Frequency Spectrum of Composite Waveform with Attenuated Harmonics')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')
plt.grid(True)

# Annotate the harmonics
for n in range(1, num_harmonics + 1):
    freq = fundamental_freq * n
    # Find the index of the frequency closest to the harmonic
    idx = np.argmin(np.abs(xf - freq))
    # Get the amplitude at this frequency
    amplitude = 2.0 / N * np.abs(yf[idx])
    # Place the text slightly above the peak
    plt.text(freq, amplitude * 1.1, f'{note_names[n - 1]} ({freq:.2f} Hz)', color=colors[n - 1],
             horizontalalignment='center', verticalalignment='bottom')

# Set x-axis limits to include the fundamental frequency and slightly beyond the last harmonic
plt.xlim(fundamental_freq * 0.8, fundamental_freq * (num_harmonics + 1))

plt.tight_layout()
plt.savefig('harmonic_spectrum_attenuated_labeled.png')
plt.show()
