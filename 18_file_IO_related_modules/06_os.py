import os   
# os.mkdir('new_folder')  # creates a new directory named 'new_folder'
# os.rename('new_folder', 'renamed_folder')  # renames 'new_folder' to 'renamed_folder'
# os.remove('renamed_folder')  # removes the directory named 'renamed_folder'

a = os.getcwd()  # gets the current working directory
print(a)  # prints the current working directory
b = os.listdir()  # lists all files and directories in the current working directory
print(b)  # prints the list of files and directories in the current working directory   

print(os.path.exists('06_os.py'))  # checks if the file '06_os.py' exists in the current working directory
print(os.path.isfile('06_os.py'))  # checks if '06_os.py' is a file

# os.rmdir('renamed_folder')  # removes the directory named 'renamed_folder' (only if it's empty)

# os.makedirs('parent_folder/child_folder')  # creates a directory named 'parent_folder' with a subdirectory named 'child_folder'
# os.removedirs('parent_folder/child_folder')  # removes the directory 'child_folder' and then removes 'parent_folder' if it's empty