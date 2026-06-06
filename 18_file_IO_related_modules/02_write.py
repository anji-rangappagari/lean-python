#  write file caled John Doe.txt
# It should contain data about John Doe

f = open("John Doe.txt", "w")
string = '''
Name: John Doe
Age: 30
Occupation: Software Developer
'''

f.write(string)
f.close()
