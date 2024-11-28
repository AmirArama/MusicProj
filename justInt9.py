import matplotlib.pyplot as plt
import numpy as np

# Original data
first_arc = [('C', 0), ('G', 30), ('D', 60), ('A', 90), ('E', 120), ('B', 150), 
             ('F#', 180), ('Db', 210), ('Ab', 240), ('Eb', 270), ('Bb', 300), 
             ('F', 330), ('C', 360)]

value_to_add = 0.2
second_arc = [(note, angle + (index * value_to_add)) for index, (note, angle) in enumerate(first_arc)]

# Function to plot a single circle with dots
def plot_circle_with_dots(ax, first_arc, second_arc, center, radius):
    # Draw the red circle
    circle = plt.Circle(center, radius, color='red', fill=False, linewidth=6)
    ax.add_artist(circle)
    
    # Plot the first_arc dots (blue) and labels
    for note, angle in first_arc:
        # Convert angle to radians
        angle_rad = np.radians(90 - angle)
        
        # Dot positions
        x = center[0] + radius * np.cos(angle_rad)
        y = center[1] + radius * np.sin(angle_rad)
        ax.scatter(x, y, color='blue', s=50, zorder=5,linewidth=3)
        
        # Label positions (radius + 0.1)
        label_x = center[0] + (radius + 0.15) * np.cos(angle_rad)
        label_y = center[1] + (radius + 0.15) * np.sin(angle_rad)
        ax.text(label_x, label_y, note, fontsize=18, ha='center', va='center', color='blue')
    
    # Plot the second_arc dots (green) and labels
    for note, angle in second_arc:
        # Convert angle to radians
        angle_rad = np.radians(90 - angle)
        
        # Dot positions
        x = center[0] + (radius-0.1) * np.cos(angle_rad)
        y = center[1] + (radius-0.1) * np.sin(angle_rad)
        ax.scatter(x, y, color='green', s=50, zorder=5,linewidth=3)
        
        # Label positions (radius - 0.1)
        label_x = center[0] + (radius - 0.25) * np.cos(angle_rad)
        label_y = center[1] + (radius - 0.25) * np.sin(angle_rad)
        ax.text(label_x, label_y, note, fontsize=18, ha='center', va='center', color='green')
    
    # Set aspect ratio
    ax.set_aspect('equal', adjustable='datalim')
    ax.axis('off')  # Turn off the axis

# Create the figure and axes
fig, ax = plt.subplots(figsize=(8, 8))

# Plot the circle and dots for both lists
plot_circle_with_dots(
    ax=ax, 
    first_arc=first_arc, 
    second_arc=second_arc, 
    center=(0, 0), 
    radius=1
)

# Set the limits and display the plot
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
plt.tight_layout()

# Save the plot as a transparent PNG
plt.tight_layout()
plt.savefig("circle_plot_transparent.png", dpi=300, transparent=True)

plt.show()
