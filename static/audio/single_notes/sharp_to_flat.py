import os
import shutil

# Define the mapping for sharp to flat notes
sharp_to_flat_mapping = {
    "C_sharp": "D_flat",
    "D_sharp": "E_flat",
    "F_sharp": "G_flat",
    "G_sharp": "A_flat",
    "A_sharp": "B_flat"
}

# Path to your audio directory
audio_directory = os.getcwd()  # Current working directory

# Iterate over all files in the directory
for filename in os.listdir(audio_directory):
    if "_sharp" in filename and filename.endswith(".mp3"):
        # Parse the string to extract components
        parts = filename.split("_")
        string = parts[0]  # e.g., "string6"
        note_with_octave = parts[1]  # e.g., "G3"
        sharp_flat = parts[2].replace(".mp3", "")  # e.g., "sharp"

        # Split note into base note and octave (e.g., "G3" -> "G", "3")
        base_note = note_with_octave[:-1]  # Extract the note (e.g., "G")
        octave = note_with_octave[-1]  # Extract the octave (e.g., "3")

        # Check if the sharp note has a corresponding flat
        sharp_key = f"{base_note}_sharp"
        if sharp_key in sharp_to_flat_mapping:
            # Get the corresponding flat note
            flat_note = sharp_to_flat_mapping[sharp_key]
            flat_base_note, flat_modifier = flat_note.split("_")

            # Construct the new filename (no octave adjustment)
            new_filename = f"{string}_{flat_base_note}{octave}_flat.mp3"
            source_path = os.path.join(audio_directory, filename)
            destination_path = os.path.join(audio_directory, new_filename)

            # Copy the file and rename it
            shutil.copy(source_path, destination_path)
            print(f"Copied and renamed: {filename} -> {new_filename}")

print("All sharp notes have been copied and renamed to flats.")
