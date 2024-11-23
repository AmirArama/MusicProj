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
    text_colors,          # Nested list of text colors per arc level
    text_sizes=None,      # List of font sizes per arc (nested list)
    transparent_levels=None,  # List of levels to make fully transparent
    exclude_levels=None,  # List of levels to exclude entirely
    rotate_text_levels=None,  # List of levels to rotate text radially
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
    if rotate_text_levels is None:
        rotate_text_levels = []

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
            text_color = text_colors[i][j % len(text_colors[i])]  # Text color for this arc

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

            # Determine rotation for text
            rotation_angle = theta - 90 if i in rotate_text_levels else 0

            text_element = ax.text(
                x_text, y_text, text,
                ha="center", va="center",
                fontsize=text_size,  # Font size for this specific arc
                color=text_color,    # Use specified text color
                rotation=rotation_angle,  # Rotate text radially for specific levels
                alpha=1.0,           # Ensure full opacity
                weight='bold'        # Make the text bold
            )
            text_element.set_path_effects([
                path_effects.Stroke(linewidth=2, foreground="white"),
                path_effects.Normal()
            ])  # Add white outline for better contrast

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
    
def replace_non_empty_positions(list1, list2):
    # Ensure both lists have the same length
    if len(list1) != len(list2):
        raise ValueError("Both lists must have the same length.")
    
    # Replace elements in list1 with corresponding non-empty elements in list2
    result = [
        list2[i] if list2[i] != "" else list1[i]
        for i in range(len(list1))
    ]
    return result

def combine_with_subscript_matplotlib(primary_list, subscript_list):
    """
    Combines two lists by adding subscripts to the primary_list elements
    from the subscript_list where the subscript_list is not empty.

    Args:
        primary_list (list of str): The main list of strings.
        subscript_list (list of str): The subscript list of strings.

    Returns:
        list of str: A new list with combined elements formatted for matplotlib.
    """
    combined = []
    for primary, subscript in zip(primary_list, subscript_list):
        if subscript:  # If subscript is not empty
            combined.append(f"{primary}$_{{{subscript}}}$")
        else:
            combined.append(primary)  # Keep the primary text unchanged
    return combined


# Example usage
radius = 12
radial_splits = [0, 4, 6, 8, 10, 11]
angular_splits = [12, 12, 12, 12, 12, 12]
colors = [
    ["#CCCCCC"] * 12,
    ["#CCCCCC"] * 12,
    ["#CCCCCC"] * 12,
    ["#CCCCCC"] * 12,
    ["#CCCCCC"] * 12
]

colors[1][len(colors[2])-1] = "#88E788"
colors[1][len(colors[2])-2] = "#88E788"
colors[1][0] = "#88E788"

colors[2][len(colors[2])-1] = "#6598DF"
colors[2][len(colors[2])-2] = "#6598DF"
colors[2][0] = "#6598DF"

colors[3][len(colors[2])-1] = "#FC6A21"

text_colors = [
    ["black"] * 12,
    ["black"] * 12,
    ["black"] * 12,
    ["black"] * 12,
    ["black"] * 12
]
text_colors[2] = shift_list(text_colors[2], 3, "right")
text_colors[1][len(text_colors[1])-1] = "red"
text_colors[2][2] = "red"
text_colors[3][4] = "red"


major = ["C", "G", "D", "A", "E", "B", "F#", "Db", "Ab", "Eb", "Bb", "F"]
minor = ["Am", "Em", "Bm", "F#m", "C#m", "G#m", "Ebm", "Bbm", "Fm", "Cm", "Gm", "Dm"]
locrian = ["B" + "\u00B0", "F#" + "\u00B0", "C#" + "\u00B0", "G#" + "\u00B0", "D#" + "\u00B0",
            "A#" + "\u00B0", "F" + "\u00B0", "C" + "\u00B0", "G" + "\u00B0", "D" + "\u00B0", 
            "A" + "\u00B0","E" + "\u00B0"]

minor.reverse()
major.reverse()
locrian.reverse()

major_add = ["Ion", "Mix", "", "", "", "", "", "", "", "", "", "Lyd"]
minor_add = ["Aeo", "Phr", "", "", "", "", "", "", "", "", "", "Dor"]
locrian_add = ["Loc", "", "", "", "", "", "", "", "", "", "", ""]

#major_add = ["I", "V", "", "", "", "", "", "", "", "", "", "IV"]
#minor_add = ["vi", "iii", "", "", "", "", "", "", "", "", "", "ii"]
#locrian_add = ["vii", "", "", "", "", "", "", "", "", "", "", ""]

minor_add.reverse()
major_add.reverse()
locrian_add.reverse()

scale_rev = copy.deepcopy(major)
scale_rev.reverse()

mds = ["Ionian", "Mixolydian", "Dorian", "Aeolian", "Phrygian", "Locrian", "","","","","", "Lydian"]
mds = shift_list(mds, 1, "left")


for i in range(len(major)):
    colors_shifted = copy.deepcopy(colors)
    colors_shifted[1] = shift_list(colors_shifted[1], i, "left")
    colors_shifted[2] = shift_list(colors_shifted[2], i, "left")
    colors_shifted[3] = shift_list(colors_shifted[3], i, "left")

    mds_shifted = copy.deepcopy(mds)
    mds_shifted = shift_list(mds_shifted, i, "left")

    text_colors_shifted = copy.deepcopy(text_colors)
    text_colors_shifted[1] = shift_list(text_colors_shifted[1], i, "left")
    text_colors_shifted[2] = shift_list(text_colors_shifted[2], i, "left")
    text_colors_shifted[3] = shift_list(text_colors_shifted[3], i, "left")

    major_add_shifted = copy.deepcopy(major_add)
    minor_add_shifted = copy.deepcopy(minor_add)
    locrian_add_shifted = copy.deepcopy(locrian_add)


    major_add_shifted = shift_list(major_add_shifted, i, "left")
    minor_add_shifted = shift_list(minor_add_shifted, i, "left")
    locrian_add_shifted = shift_list(locrian_add_shifted, i, "left")


    #major_replaced = replace_non_empty_positions(major,major_add_shifted)
    major_replaced = combine_with_subscript_matplotlib(major,major_add_shifted)
    minor_replaced = combine_with_subscript_matplotlib(minor,minor_add_shifted)
    locrian_replaced = combine_with_subscript_matplotlib(locrian,locrian_add_shifted)





    texts = [
        [""] * 12,
        major_replaced,
        minor_replaced,
        locrian_replaced,
        mds_shifted
    ]    

    text_sizes = [
        [24] * 12,
        [18] * 12,
        [18] * 12,
        [18] * 12,
        [24] * 12,
    ]

    create_circle_diagram(
        radius=radius,
        radial_splits=radial_splits,
        angular_splits=angular_splits,
        colors=colors_shifted,
        texts=texts,
        text_colors=text_colors_shifted,
        text_sizes=text_sizes,
        transparent_levels=[4],
        exclude_levels=[0],
        rotate_text_levels=[1,2,3,4],  # Rotate text for outer arc (level 1)
        spacing_angle_ratio=0.05,
        spacing_radius=0.1,
        output_folder="circle_of_fifths_mode_key_" + str(scale_rev[i]),
        save_transparent=True
    )
