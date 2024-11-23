import matplotlib.pyplot as plt
from matplotlib.patches import Wedge
import os
import numpy as np
import matplotlib.patheffects as path_effects  # Import for text outline effect
import copy


def create_circle_diagram(
    radius,               # Overall radius
    radial_splits,        # List for radial depths [r1, r2, r3, ...]
    angular_splits,       # List of segments for each depth [n1, n2, n3, ...]
    colors,               # List of colors for each segment
    texts,                # List of texts for each segment
    text_colors="black",  # List of text colors per level or single color
    text_sizes=None,      # List of font sizes per arc (nested list)
    transparent_levels=None,  # List of levels to make fully transparent
    exclude_levels=None,  # List of levels to exclude entirely
    spacing_angle_ratio=0.05,  # Ratio of spacing to angular step (constant relative spacing)
    spacing_radius=0.0,   # Spacing between radial levels
    output_folder="circle_diagram",  # Folder to save transparent images
    save_transparent=True # Save transparent elements separately
):
    if exclude_levels is None:
        exclude_levels = []
    if text_sizes is None:
        # Default to size 14 for all arcs if no font sizes are provided
        text_sizes = [[14] * angular_splits[i] for i in range(len(radial_splits) - 1)]
    if transparent_levels is None:
        transparent_levels = []
    if isinstance(text_colors, str):
        text_colors = [text_colors] * len(radial_splits)  # Single color applied to all levels

    os.makedirs(output_folder, exist_ok=True)  # Ensure output directory exists
    full_image_data = []  # To store data for reconstruction

    # Set up the figure for the full diagram
    fig, ax = plt.subplots(figsize=(10, 10), dpi=300)
    ax.set_aspect("equal")
    ax.axis("off")  # Turn off axes for clarity

    # Set axis limits to fit the entire diagram
    max_radius = max(radial_splits)
    ax.set_xlim(-max_radius, max_radius)
    ax.set_ylim(-max_radius, max_radius)

    # Loop through radial depths
    for i, (start_radius, end_radius) in enumerate(zip(radial_splits[:-1], radial_splits[1:])):
        if i in exclude_levels:  # Skip excluded levels entirely
            continue
        
        n_segments = angular_splits[i]  # Number of angular segments at this depth
        angle_step = 360 / n_segments   # Angle covered by each segment
        spacing_angle = angle_step * spacing_angle_ratio  # Dynamic angular spacing

        for j in range(n_segments):
            # Compute angles for the segment
            start_angle = j * angle_step + spacing_angle / 2 + angle_step / 2 + 90
            end_angle = (j + 1) * angle_step - spacing_angle / 2 + angle_step / 2 + 90

            # Adjust radii for spacing
            inner_radius = start_radius + spacing_radius / 2
            outer_radius = end_radius - spacing_radius / 2

            # Get color, text, and font size for this segment
            color = "none" if i in transparent_levels else colors[i][j % len(colors[i])]
            text = texts[i][j % len(texts[i])]
            text_size = text_sizes[i][j]  # Font size for this specific arc
            text_color = text_colors[i]  # Text color for this level

            # Draw the wedge
            wedge = Wedge(
                center=(0, 0),
                r=outer_radius,
                theta1=start_angle,
                theta2=end_angle,
                width=outer_radius - inner_radius,
                facecolor=color if color != "none" else "none",
                edgecolor="black",
                alpha=1.0 if color != "none" else 0.0  # Hide edges if fully transparent
            )
            ax.add_patch(wedge)

            # Add the text with outline
            theta = (start_angle + end_angle) / 2  # Midpoint angle for text
            text_radius = (inner_radius + outer_radius) / 2
            x_text = text_radius * np.cos(np.radians(theta))
            y_text = text_radius * np.sin(np.radians(theta))
            
            text_element = ax.text(
                x_text, y_text, text,
                ha="center", va="center",
                fontsize=text_size,  # Font size for this specific arc
                color=text_color,    # Use specified text color
                rotation=0,          # No rotation
                alpha=1.0            # Ensure full opacity
            )
            text_element.set_path_effects([
                path_effects.Stroke(linewidth=2, foreground="white"),
                path_effects.Normal()
            ])  # Add white outline for better contrast

            # Save transparent image for this segment (if enabled)
            if save_transparent:
                element_fig, element_ax = plt.subplots(figsize=(10, 10), dpi=300)
                element_ax.set_aspect("equal")
                element_ax.axis("off")
                element_ax.set_xlim(-max_radius, max_radius)
                element_ax.set_ylim(-max_radius, max_radius)

                element_ax.add_patch(Wedge(
                    center=(0, 0),
                    r=outer_radius,
                    theta1=start_angle,
                    theta2=end_angle,
                    width=outer_radius - inner_radius,
                    facecolor=color if color != "none" else "none",
                    edgecolor="black" if color != "none" else "none",
                    alpha=1.0 if color != "none" else 0.0
                ))

                text_element = element_ax.text(
                    x_text, y_text, text,
                    ha="center", va="center",
                    fontsize=text_size,  # Match arc-specific text size
                    color=text_color,    # Match level-specific text color
                    rotation=0,          # No rotation
                    alpha=1.0            # Ensure full opacity
                )
                text_element.set_path_effects([
                    path_effects.Stroke(linewidth=2, foreground="white"),
                    path_effects.Normal()
                ])  # Add white outline for better contrast

                element_path = os.path.join(output_folder, f"segment_{i}_{j}.png")
                element_fig.savefig(element_path, transparent=True, bbox_inches="tight", pad_inches=0)
                plt.close(element_fig)

                full_image_data.append({
                    "file": element_path,
                    "center": (0, 0),
                    "radius": (inner_radius, outer_radius),
                    "angles": (start_angle, end_angle),
                    "text": text
                })

    full_image_path = os.path.join(output_folder, "full_image.png")
    fig.savefig(full_image_path, bbox_inches="tight", transparent=True)
    plt.close(fig)
    
    return full_image_path, full_image_data


def shift_list(lst, shift_by, direction="left"):
    if not lst:
        return lst  # Empty list remains empty
    
    shift_by = shift_by % len(lst)  # Ensure the shift_by is within the list length
    
    if direction == "right":
        return lst[-shift_by:] + lst[:-shift_by]
    elif direction == "left":
        return lst[shift_by:] + lst[:shift_by]
    else:
        raise ValueError("Direction must be 'left' or 'right'")


# Example usage
radius = 10
radial_splits = [0, 1, 3, 5, 7,9]
angular_splits = [12, 12, 12, 12, 12, 12]
colors = [
    ["#FF6961"]*12,
    ["#FF6961"]*12,
    ["#FF6961", "#CCCCCC", "#CCCCCC", "#CCCCCC", "#CCCCCC", "#CCCCCC", "#CCCCCC", "#6FC276", "#6FC276", "#6FC276", "#FF6961", "#FF6961"],
    ["#FF6961", "#CCCCCC", "#CCCCCC", "#CCCCCC", "#CCCCCC", "#CCCCCC", "#CCCCCC", "#6FC276", "#6FC276", "#6FC276", "#FF6961", "#FF6961"],
    ["#FF6961"]*12
]


major = ["C", "G", "D", "A", "E", "B", "F#", "Db", "Ab", "Eb", "Bb", "F"]
major.reverse()
minor = ["Am", "Em", "Bm", "F#m", "C#m", "G#m", "Ebm", "Bbm", "Fm", "Cm", "Gm", "Dm"]
minor.reverse()
majorDeg = ["I","V","","","","","","","","","","IV"]
majorDeg.reverse()
minDeg = ["vi","iii","","","","","","","","","","ii"]
minDeg.reverse()

scale_rev = copy.deepcopy(major)
scale_rev.reverse()

for i in range(len(major)):
    
    print(i)
    majorDeg_shifted = copy.deepcopy(majorDeg)
    majorDeg_shifted= shift_list(majorDeg_shifted,i)
    
    minDeg_shifted = copy.deepcopy(minDeg)
    minDeg_shifted = shift_list(minDeg_shifted,i)

    colors_shifted = copy.deepcopy(colors)
 
    colors_shifted[2] = shift_list(colors_shifted[2],i)
    print(colors_shifted[2])
    colors_shifted[3] = shift_list(colors_shifted[3],i)
    #colors_shifted[2].reverse()
    #colors_shifted[3].reverse()

    texts = [
        [""]*12,
        minDeg_shifted,
        minor,
        major,
        majorDeg_shifted,
    ]

    # Specify different text sizes for each arc
    text_sizes = [
        [20]*12,  # Font sizes for level 0
        [20]*12,  # Font sizes for level 1
        [24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24],  # Font sizes for level 2
        [32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32],  # Font sizes for level 3
        [20]*12,  # Font sizes for level 4

    ]

    tcolor = ["black", "black", "black","black","black"]
    print(scale_rev[i])
    create_circle_diagram(
        radius=radius,
        radial_splits=radial_splits,
        angular_splits=angular_splits,
        colors=colors_shifted,
        texts=texts,
        text_colors=tcolor,  # Specify text colors
        text_sizes=text_sizes,  # Specify font sizes for each arc
        transparent_levels=[1,4],  # Make level 2 arcs fully transparent
        exclude_levels=[0],      # Exclude level 1
        spacing_angle_ratio=0.05,
        spacing_radius=0.1,
        output_folder="circle_of_fifths_key_"+str(scale_rev[i]),
        save_transparent=True
    )
