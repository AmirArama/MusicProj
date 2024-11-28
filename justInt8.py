import matplotlib.pyplot as plt
import numpy as np

first_arc = [('C', 0), ('G', 30), ('D', 60), ('A', 90), ('E', 120), ('B', 150), ('F#', 180), ('Db', 210), ('Ab', 240), ('Eb', 270), ('Bb', 300), ('F', 330), ('C', 360)]

value_to_add = 0.2
second_arc = [(note, angle + (index * value_to_add)) for index, (note, angle) in enumerate(first_arc)]

# Define the function to draw arcs with dots
def draw_arc(ax, arc_data, center, radius, color, label):
    for i in range(len(arc_data) - 1):
        start_angle = arc_data[i][1]
        end_angle = arc_data[i + 1][1]
        
        # Calculate arc points
        theta = np.linspace(np.radians(90 - start_angle), np.radians(90 - end_angle), 100)
        x = center[0] + radius * np.cos(theta)
        y = center[1] + radius * np.sin(theta)
        ax.plot(x, y, color=color, linewidth=4)
        
        # Add a dot at the start position of each arc
        start_angle_rad = np.radians(90 - start_angle)
        x_start = center[0] + radius * np.cos(start_angle_rad)
        y_start = center[1] + radius * np.sin(start_angle_rad)
        ax.scatter(x_start, y_start, color=color, s=30, zorder=5, linewidth=5)  # Add a dot (scatter point)

        start_angle_rad = np.radians(90 - end_angle)
        x_start = center[0] + radius * np.cos(start_angle_rad)
        y_start = center[1] + radius * np.sin(start_angle_rad)
        ax.scatter(x_start, y_start, color="red", s=30, zorder=5, linewidth=5)  # Add a dot (scatter point)


    # Add labels
    for (name, angle) in arc_data:
        angle_rad = np.radians(90 - angle)  # Adjust for counterclockwise
        x = center[0] + (radius+0.2) * np.cos(angle_rad)
        y = center[1] + (radius+0.2) * np.sin(angle_rad)
        ax.text(x, y, name, fontsize=18, ha='center', va='center', color=color)
    ax.set_aspect('equal', adjustable='datalim')
    #ax.set_title(label)

# Create the figure and axes
fig, axes = plt.subplots(1, 2, figsize=(10, 5))

# Plot first arc with dots
draw_arc(
    ax=axes[0],
    arc_data=first_arc,
    center=(0, 0),
    radius=1,
    color='blue',
    label='First Arc'
)

# Plot second arc with dots
draw_arc(
    ax=axes[1],
    arc_data=second_arc,
    center=(0, 0),
    radius=1,
    color='green',
    label='Second Arc'
)

# Adjust layout and display the plot
# Add this line to remove axes for each subplot
axes[0].axis('off')  # Removes axes for the first arc
axes[1].axis('off')  # Removes axes for the second arc

plt.tight_layout()
plt.show()
