# line by line reading of a file

f = open("John Doe.txt", "r")
line = f.readline()
for i in range(5):
    print(line, end='')
    line = f.readline()
f.close()