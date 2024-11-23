import os

# Update this path to the local directory where your files are stored
directory = "notes_no_sharp"

# Function to rename files
def rename_files(directory):
    for filename in os.listdir(directory):
        new_filename = filename
        
        # Replace sharps (#) with "_sharp"
        if "#.png" in filename:
            new_filename = new_filename.replace("#", "_sharp")
        
        # Replace flats (b) with "_flat"
        if "b.png" in filename and not "Bb" in filename:
            new_filename = new_filename.replace("b", "_flat")
        elif "Bb.png" in filename:
            new_filename = new_filename.replace("Bb", "_flatB")
        
        # Only rename if the filename has changed
        if filename != new_filename:
            original_path = os.path.join(directory, filename)
            new_path = os.path.join(directory, new_filename)
            os.rename(original_path, new_path)
            print(f"Renamed: {filename} -> {new_filename}")

# Run the renaming function
rename_files(directory)
