import os
from pydub import AudioSegment

def convert_wav_to_mp3(input_folder, output_folder, bitrate="128k"):
    """
    Converts all WAV files in the input folder to MP3 format.

    Args:
        input_folder (str): Path to the folder containing WAV files.
        output_folder (str): Path to the folder where MP3 files will be saved.
        bitrate (str): Desired MP3 bitrate (e.g., "128k", "192k").
    """
    # Ensure the output folder exists
    os.makedirs(output_folder, exist_ok=True)

    # Process all WAV files in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith(".wav"):
            input_path = os.path.join(input_folder, filename)
            output_filename = os.path.splitext(filename)[0] + ".mp3"
            output_path = os.path.join(output_folder, output_filename)

            # Convert WAV to MP3
            try:
                print(f"Converting {filename} to MP3...")
                audio = AudioSegment.from_file(input_path)
                audio.export(output_path, format="mp3", bitrate=bitrate)
                print(f"Saved: {output_path}")
            except Exception as e:
                print(f"Error converting {filename}: {e}")

# Define the input and output directories
input_folder = "note_files/notes"  # Replace with the folder containing your WAV files
output_folder = "note_files/mp3_notes"  # Replace with the desired output folder

# Convert WAV to MP3
convert_wav_to_mp3(input_folder, output_folder)
