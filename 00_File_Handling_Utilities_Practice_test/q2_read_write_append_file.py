# 2. Read, Write, and Append Files
# Write a program that writes three lines of text to a file tasks.txt.
# Open tasks.txt in append mode and add a new line "Task Completed!".
# Read the file and print all lines as a list using readlines().

with open("FILE.txt", "w") as f:
    content = "Learning Python is fun!\
        it's good experince to learn python\
        after a long time i am learning python"
    f.write(content)


with open("FILE.txt", "r") as f:
    content = f.read()
    print(content)

with open("FILE.txt", "a") as f:
    additional_content = "\nPython is a versatile language."
    f.write(additional_content)


with open("FILE.txt", "r") as f:
    content = f.read()
    print(content)