import matplotlib.pyplot as plt
import numpy as np

# Define the segments for a 16-segment display layout
segments = {
    'A': [1, 2, 3, 4, 5, 6, 7, 10, 11, 12, 13],
    'B': [1, 2, 3, 4, 6, 7, 8, 11, 12, 13, 14, 15],
    'C': [1, 2, 7, 8, 9, 10],
    'D': [1, 2, 3, 4, 6, 8, 9, 12, 13, 15],
    'E': [1, 2, 5, 6, 7, 8, 9, 10, 14],
    'F': [1, 5, 6, 7, 8, 10]
}

# Define positions of each segment for a 16-segment display layout
# This layout assumes segments numbered 1 through 16 in a rectangular arrangement
segment_positions = {
    1: ((0.2, 1.6), (0.8, 1.6)),  # Top horizontal
    2: ((0.8, 1.6), (1.2, 1.2)),  # Top-right diagonal
    3: ((1.2, 1.2), (1.2, 0.8)),  # Right vertical upper
    4: ((1.2, 0.8), (0.8, 0.4)),  # Bottom-right diagonal
    5: ((0.8, 0.4), (0.2, 0.4)),  # Bottom horizontal
    6: ((0.2, 0.4), (0, 0.8)),    # Bottom-left diagonal
    7: ((0, 0.8), (0, 1.2)),      # Left vertical upper
    8: ((0, 1.2), (0.2, 1.6)),    # Top-left diagonal
    9: ((0.2, 1), (0.8, 1)),      # Middle horizontal
    10: ((0.8, 1.6), (1, 1.4)),   # Extra top-right diagonal
    11: ((1, 1.4), (1.2, 1)),     # Extra right vertical
    12: ((1.2, 1), (1, 0.6)),     # Extra bottom-right diagonal
    13: ((1, 0.6), (0.8, 0.4)),   # Bottom-right fill
    14: ((0, 1), (0.2, 1)),       # Left vertical lower
    15: ((0, 0.8), (0.2, 0.6)),   # Extra bottom-left diagonal
    16: ((0.2, 0.6), (0.8, 0.6))  # Bottom-left fill
}

# Function to draw a character on a 16-segment display
def draw_character(segments_on, ax):
    for seg in segments_on:
        p1, p2 = segment_positions[seg]
        ax.plot([p1[0], p2[0]], [p1[1], p2[1]], color='lime', linewidth=8)
    ax.set_xlim(-0.2, 1.4)
    ax.set_ylim(0, 2)
    ax.axis('off')

# Plot the characters
fig, axes = plt.subplots(1, 6, figsize=(12, 3))
fig.patch.set_facecolor('black')
letters = ['A', 'B', 'C', 'D', 'E', 'F']

for i, letter in enumerate(letters):
    ax = axes[i]
    ax.set_facecolor('black')
    if letter in segments:
        draw_character(segments[letter], ax)
    ax.set_title(letter, color='white', fontsize=18)

plt.show()
