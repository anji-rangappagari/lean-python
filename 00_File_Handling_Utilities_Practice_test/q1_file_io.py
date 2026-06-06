# 1. File I/O Basics
# Create a text file notes.txt using Python and write "Learning Python is fun!" into it.
# Open notes.txt, read its content, and print it to the console

file_name = "notes.txt"
# Write to the file
with open(file_name, 'w') as file:
    file.write("Learning Python is fun!")

# Read from the file
with open(file_name, 'r') as file:
    content = file.read()
    print(content)

f = open("FILE.txt", "w")
content = "Learning Python is fun!"
f.write(content)
f.close()