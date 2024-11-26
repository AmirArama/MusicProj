import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq

# Fundamental frequency for A4
fundamental_freq = 440.0  # Hz

# Sampling parameters
sampling_rate = 44100  # Samples per second
duration = 0.002295        # Duration in seconds for each waveform

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
plt.rcParams['legend.fontsize'] = 18
# Add legend with transparent background and custom font size
ax.legend(loc='upper right', framealpha=0, fontsize='x-small')  # Large font size


# Add legend with transparent background
ax.legend(loc='upper right', framealpha=0)


# Set figure background to transparent
fig.patch.set_alpha(0)

# Save the plot as a PNG file with transparent background
plt.tight_layout()
plt.savefig('individual_harmonics_transparent.png', transparent=True)
plt.show()
