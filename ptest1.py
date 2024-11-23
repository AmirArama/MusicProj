import matplotlib.pyplot as plt
from matplotlib.patches import Wedge
import os

# Function to create a pie segment image
def create_pie_segment(filename, theta_start, theta_end, color):
    fig, ax = plt.subplots(figsize=(4, 4), dpi=100)
    ax.set_aspect('equal')

    # Add a wedge for the pie segment
    wedge = Wedge(center=(0, 0), r=1, theta1=theta_start, theta2=theta_end, facecolor=color, alpha=0.8)
    ax.add_patch(wedge)

    # Remove axes and background
    ax.axis('off')
    ax.set_xlim(-1.1, 1.1)
    ax.set_ylim(-1.1, 1.1)

    # Save the image as a transparent PNG
    plt.savefig(filename, transparent=True)
    plt.close(fig)

# Create 12 segments for the Circle of Fifths
output_dir = "pie_segments"
os.makedirs(output_dir, exist_ok=True)
colors = ["red", "green", "blue", "orange", "purple", "yellow", "cyan", "pink", "lime", "teal", "magenta", "gray"]

for i in range(12):
    theta1 = i * 30  # Start angle (30 degrees per segment)
    theta2 = theta1 + 30  # End angle
    filename = f"{output_dir}/segment_{i}.png"
    create_pie_segment(filename, theta1, theta2, colors[i % len(colors)])
