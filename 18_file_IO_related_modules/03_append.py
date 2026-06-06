#  Append to an exosting file called John Doe.txt
# It should contain data about John Doe's hobbies

f = open("John Doe.txt", "a")
string = '''
Hobbies:
- Reading
- Hiking
- Coding
'''
f.write(string)
f.close()
