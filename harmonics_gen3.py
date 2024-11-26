import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq

# Fundamental frequency for A4
fundamental_freq = 440.0  # Hz

# Sampling parameters
sampling_rate = 44100  # Samples per second
duration = 0.1      # Duration in seconds for each waveform

# Time array
t = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False)

# Number of harmonics to display
num_harmonics = 8

# Corresponding note names for the first eight harmonics
note_names = ['A4', 'A5', 'E6', 'A6', 'C♯7', 'E7', 'G7', 'A7']

# Colors for each harmonic
colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'orange']

# Initialize the composite waveform
composite_waveform = np.zeros_like(t)

# Create a figure for individual harmonics
fig, ax = plt.subplots(figsize=(12, 8))

for n in range(1, num_harmonics + 1):
    # Frequency of the nth harmonic
    freq = fundamental_freq * n
    # Amplitude scaling factor (1/n)
    amplitude = 1 / n
    # Generate the waveform for the nth harmonic
    waveform = amplitude * np.sin(2 * np.pi * freq * t)
    # Add to the composite waveform
    composite_waveform += waveform
    # Plot the waveform with decreasing line width
    ax.plot(t, waveform, color=colors[n - 1], linewidth=6 / n, label=f'{note_names[n - 1]} ({freq:.2f} Hz)')

# Remove axes and grid
ax.axis('off')

# Add legend
ax.legend(loc='upper right')

# Set figure background to transparent
fig.patch.set_alpha(0)

# Save the plot as a PNG file with transparent background
plt.tight_layout()
plt.savefig('individual_harmonics_transparent.png', transparent=True)
plt.show()

# Plot the composite waveform
fig, ax = plt.subplots(figsize=(12, 6))
ax.plot(t, composite_waveform, color='b', linewidth=2)
ax.set_xlabel('Time (seconds)')
ax.set_ylabel('Amplitude')
ax.set_title('Composite Waveform of A4 and Its Harmonics')
ax.grid(True)

# Set figure background to transparent
fig.patch.set_alpha(0)

# Save the composite waveform plot as a PNG file with transparent background
plt.tight_layout()
plt.savefig('composite_waveform_transparent.png', transparent=True)
plt.show()

# Perform Fourier Transform on the composite waveform
N = len(t)
yf = fft(composite_waveform)
xf = fftfreq(N, 1 / sampling_rate)[:N // 2]

# Plot the frequency spectrum
fig, ax = plt.subplots(figsize=(12, 6))
ax.plot(xf, 2.0 / N * np.abs(yf[:N // 2]), 'b')
ax.set_xlabel('Frequency (Hz)')
ax.set_ylabel('Amplitude')
#ax.set_title('Frequency Spectrum of Composite Waveform')
ax.axis('off')
ax.grid(True)

# Annotate the harmonics without arrows
for n in range(1, num_harmonics + 1):
    freq = int(fundamental_freq * n)
    # Find the index of the frequency closest to the harmonic
    idx = np.argmin(np.abs(xf - freq))
    # Get the amplitude at this frequency
    amplitude = 2.0 / N * np.abs(yf[idx])
    # Place the text slightly above the peak
    plt.rcParams['legend.fontsize'] = 50

    ax.text(freq, amplitude * 1.1, f'{note_names[n - 1]}-{freq}Hz', color=colors[n - 1],
            horizontalalignment='center', verticalalignment='bottom',fontsize="xx-large")

# Set x-axis limit to slightly beyond the last harmonic
ax.set_xlim(0, fundamental_freq * (num_harmonics + 1))

# Set figure background to transparent
fig.patch.set_alpha(0)

# Save the frequency spectrum plot as a PNG file with transparent background
plt.tight_layout()
plt.savefig('frequency_spectrum_transparent.png', transparent=True)
plt.show()
