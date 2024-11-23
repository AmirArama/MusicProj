import matplotlib.pyplot as plt

# Set up fretboard dimensions
num_frets = 12
num_strings = 6
fig, ax = plt.subplots(figsize=(10, 3))

# Draw strings and frets
for string in range(num_strings):
    ax.plot([0, num_frets], [string, string], 'gray', linewidth=2)  # strings
for fret in range(num_frets + 1):
    ax.plot([fret, fret], [0, num_strings - 1], 'gray', linewidth=2)  # frets

# Define note positions and intervals
notes = {
    (3, 0): 'R',  # Root
    (5, 2): 'b3', # Minor third
    (7, 3): 'p5', # Perfect fifth
    # Add more notes as needed
}

# Color coding for intervals
colors = {'R': 'blue', 'b3': 'orange', 'p5': 'green'}

# Add notes
for (fret, string), interval in notes.items():
    ax.add_patch(plt.Circle((fret, string), 0.3, color=colors[interval]))
    ax.text(fret, string, interval, color='white', ha='center', va='center', fontweight='bold')

# Customize plot
ax.set_xlim(-0.5, num_frets + 0.5)
ax.set_ylim(-0.5, num_strings - 0.5)
ax.axis('off')

# Save as PNG
plt.savefig("guitar_neck_diagram.png", dpi=300, bbox_inches='tight')
plt.show()
