# Python script to sort files in a directory by their extension
import os, sys
from shutil import move

def sort_file(directory_path):
    # Scrub through directory_path and take each file
    for filename in os.listdir(directory_path):
        # Check if file exist
        if os.path.isfile(os.path.join(directory_path,filename)):
            # Get the end of the file
            file_extension = filename.split('.')[-1]
            destination_directory = os.path.join(directory_path,file_extension)
            # Create directory destination if not exist
            if not os.path.exists(destination_directory):
                os.makedirs(destination_directory)
            # Move file for directory destination if not exist
            if not os.path.isfile(os.path.join(destination_directory, filename)):
                move(os.path.join(directory_path, filename), os.path.join(destination_directory, filename))

directory_path = sys.argv[1]

sort_file(directory_path)
