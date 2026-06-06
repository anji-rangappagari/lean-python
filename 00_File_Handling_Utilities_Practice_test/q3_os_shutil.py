# 3. OS and Shutil Modules
# Use the os module to:
# Print the current working directory
# List all files and folders in the current directory
# Create a new folder my_folder
# Use the shutil module to:
# Copy a file from one folder to another
# Move a file to a new folder
# Delete a file (careful: irreversible!)

import os
import shutil
os.mkdir("my_folder")
shutil.copy("FILE.txt", "my_folder/FILE.txt")
shutil.move("my_folder/FILE.txt", "my_folder/FILE_moved.txt")
os.remove("my_folder/FILE_moved.txt")
print("Current working directory:", os.getcwd())
print("Files and folders in the current directory:", os.listdir())
os.rmdir("my_folder")
