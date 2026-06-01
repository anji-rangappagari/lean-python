a = 22
b = "22"

print (a)  # Output: 22
print (type(a))  # Output: <class 'int'>
print (b)  # Output: "22"
print (type(b))  # Output: <class 'str'>

c = int(b)  # Convert string to integer
print (c)  # Output: 22
print (type(c))  # Output: <class 'int'>

d = str(a)  # Convert integer to string
print (d)  # Output: "22"   
print (type(d))  # Output: <class 'str'>


a = int(input ("Enter a number: "))  # Convert the input to an integer
b = int(input ("Enter a number: "))  # Convert the input to an integer
print (a + b)  # Output: Sum of the two numbers