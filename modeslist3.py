import matplotlib.pyplot as plt
import matplotlib.patches as patches

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

import copy    
notes_list = " W W H W W W H"
Ionian_notes = shift_list(copy.deepcopy(notes_list),0)
Dorian_notes = shift_list(copy.deepcopy(notes_list),2)
Phrygian_notes = shift_list(copy.deepcopy(notes_list),4)
Lydian_notes = shift_list(copy.deepcopy(notes_list),6)
Mixolydian_notes = shift_list(copy.deepcopy(notes_list),8)
Aeolian_notes = shift_list(copy.deepcopy(notes_list),10)
Locrian_notes = shift_list(copy.deepcopy(notes_list),12)



# Data for modes
modes = [
    {"name": "Ionian", "notes": Ionian_notes},
    {"name": "Dorian", "notes": Dorian_notes},
    {"name": "Phrygian", "notes": Phrygian_notes},
    {"name": "Lydian", "notes": Lydian_notes},
    {"name": "Mixolydian", "notes": Mixolydian_notes},
    {"name": "Aeolian", "notes": Aeolian_notes},
    {"name": "Locrian", "notes": Locrian_notes},
]

modes = [
    {"name": "Ionian", "notes": "I ii iii IV V vi vii°"},
    {"name": "Dorian", "notes": "i ii ♭III IV v vi° ♭VII"},
    {"name": "Phrygian", "notes": "i ♭II ♭III iv v° ♭VI ♭vii"},
    {"name": "Lydian", "notes": "I II iii ♯iv° V vi vii"},
    {"name": "Mixolydian", "notes": "I ii iii° IV v vi ♭VII"},
    {"name": "Aeolian", "notes": "i ii° ♭III iv v ♭VI ♭VII"},
    {"name": "Locrian", "notes": "i° ♭II ♭III iv ♭V ♭VI ♭vii"}
]



print(modes)

# Base colors for notes
base_colors = ["#FF6961", "#FFD700", "#77DD77", "#779ECB", "#B39EB5", "#FFB347", "#C23B22"]

# Create the figure
fig, ax = plt.subplots(figsize=(10, 6))

# Set transparent background
fig.patch.set_alpha(0)  # Make figure background transparent
ax.patch.set_alpha(0)   # Make axis background transparent

# Dimensions
x_start = 0
y_start = 7
box_width = 0.8
box_height = 0.8

# Draw modes and notes
for i, mode in enumerate(modes):
    # Rotate colors for this mode
    mode_colors = base_colors[i:] + base_colors[:i]

    # Draw mode label
    ax.text(
        x_start - 1.5,
        y_start - i,
        f"{i + 1}. {mode['name']}",
        va="center",
        ha="center",
        fontsize=20,
        bbox=dict(facecolor="black", edgecolor="none", boxstyle="round,pad=0.3"),
        color="white",
    )
    
    # Draw notes
    notes = mode["notes"].split()
    for j, note in enumerate(notes):
        rect = patches.Rectangle(
            (x_start + j * box_width + i * box_width, y_start - i - box_height / 2),
            box_width,
            box_height,
            linewidth=1,
            edgecolor="black",
            facecolor=mode_colors[j % len(mode_colors)],
        )
        ax.add_patch(rect)
        ax.text(
            x_start + j * box_width + i * box_width + box_width / 2,
            y_start - i,
            note,
            va="center",
            ha="center",
            fontsize=18,
            color="black",
            weight="bold",
        )

# Adjust the plot
ax.set_xlim(-2, 12)
ax.set_ylim(0, 8)
ax.axis("off")  # Turn off the axes

# Save the image with a transparent background
plt.tight_layout()
plt.savefig("modes_diagram_shifted_correct.png", dpi=300, transparent=True, bbox_inches="tight", pad_inches=0)
plt.show()
