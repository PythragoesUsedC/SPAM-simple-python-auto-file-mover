#SPAM The Simple Python Auto-File Mover
#make sure you have tkinter installed first then chance the CHANGE TO DESIRED PATH section
#Do make sure to be a little caredul this sorts based on the file ending

#WARNING DO NOT FORGET TO CHANGE THE CHANGE TO DESIRED PATH OR atleast # the ones you dont use stuff can mess up if not careful

import os
import shutil
import time



from tkinter import filedialog
from tkinter import *
root = Tk()
root.withdraw()
#imports

source_directory = filedialog.askdirectory()

#^^^ change this to the format source_directory = r"DESIRED PATH TO AUTO FILTER" if you perfer to run 

print(source_directory)


# Define the source directory where the files are downloaded

# Define the destination directories based on file types
destination_directories = {
    #document types
    ".txt": r"CHANGE TO DESIRED PATH",
    ".pdf": r"CHANGE TO DESIRED PATH",
    ".doc": r"CHANGE TO DESIRED PATH",
    #image types
    ".jpg": r"CHANGE TO DESIRED PATH",
    ".png": r"CHANGE TO DESIRED PATH",
    ".gif": r"CHANGE TO DESIRED PATH",
    ".webp": r"CHANGE TO DESIRED PATH",
    #vector types
    ".svg": r"CHANGE TO DESIRED PATH",
    #audio types
    ".mp3": r"CHANGE TO DESIRED PATH",
    ".wav": r"CHANGE TO DESIRED PATH",
    ".ogg": r"CHANGE TO DESIRED PATH",
    #video types
    ".mp4": r"CHANGE TO DESIRED PATH",
    ".webm": r"CHANGE TO DESIRED PATH",
    ".mov": r"CHANGE TO DESIRED PATH",
    ".mkv": r"CHANGE TO DESIRED PATH",

#add any file types desired to the above in the formate ".FILE_TYPE": r"DESIRED PATH" works for any file type
}

# Infinite loop to continuously monitor the source directory
while True:
    # Get the list of files in the source directory
    files = os.listdir(source_directory)

    # Iterate through each file
    for file in files:
        # Get the file extension
        file_extension = os.path.splitext(file)[1]

        # Check if the file extension is in the destination directories
        if file_extension in destination_directories:
            # Get the destination directory for the file type
            destination_directory = destination_directories[file_extension]

            # Move the file to the destination directory
            shutil.move(os.path.join(source_directory, file), destination_directory)

    # Sleep for a specified interval before checking again
    time.sleep(1)
    print("files sorted successfully!")
    break

#MOST CODE from the loop above IS FROM ZZZCODE SO JUST A SHOUTOUT THANK YOU, AND PLEASE SUPPORT THEM. Yes this is my first project uploaded to Github hopefully helps someone out :>
