# Using 'with' statement for file operations

with open("John Doe.txt", "r") as f:
    content = f.read()
print(content) 
# no need to call f.close() as it is automatically handled by the 'with' statement