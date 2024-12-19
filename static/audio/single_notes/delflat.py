import os

# Path to your audio directory
audio_directory = os.getcwd()
# Iterate over all files in the directory
for filename in os.listdir(audio_directory):
    if "_flat" in filename and filename.endswith(".mp3"):
        # Construct the full file path
        file_path = os.path.join(audio_directory, filename)
        
        # Delete the file
        os.remove(file_path)
        print(f"Deleted: {filename}")

print("All '_flat' files have been deleted.")