
# Arithmatic operators are used to perform mathematical operations on numbers. They are used to perform basic mathematical operations like addition, subtraction, multiplication, division, floor division, modulus and exponentiation.
a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
print("a + b =", a + b)  # Output: 11
print("a - b =", a - b)  # Output: -9
print("a * b =", a * b)  # Output: 10
print("a / b =", a / b)  # Output: 0.1
print("a // b =", a // b)  # Output: 0
print("a % b =", a % b)  # Output: 1
print("a ** b =", a ** b)  # Output: 1


# Comparison operators are used to compare two values. They return a boolean value (True or False) based on the comparison. The comparison operators are: ==, !=, >, <, >=, <=.

# a = int(input("Enter a number: "))
# b = int(input("Enter another number: "))    
print("a == b:", a == b)  # Output: False
print("a != b:", a != b)  # Output: True 
print("a > b:", a > b)  # Output: False
print("a < b:", a < b)  # Output: True  
print("a >= b:", a >= b)  # Output: False
print("a <= b:", a <= b)  # Output: True

# Logical operators are used to combine conditional statements. They return a boolean value (True or False) based on the combination of the conditions. The logical operators are: and, or, not.
# a = int(input("Enter a number: "))
# b = int(input("Enter another number: "))
print("a > 5 and b > 5:", a > 5 and b > 5)  # Output: False
print("a > 5 or b > 5:", a > 5 or b > 5)  # Output: True
print("not (a > 5):", not (a > 5))  # Output: True

# Assignment operators are used to assign values to variables. They are used to perform operations on variables and assign the result to the variable. The assignment operators are: =, +=, -=, *=, /=, //=, %=, **=.
# a = int(input("Enter a number: "))
# b = int(input("Enter another number: "))  
a += b  # a = a + b
print("a += b:", a)  # Output: 11 

a -= b  # a = a - b
print("a -= b:", a)  # Output: 1

a *= b  # a = a * b
print("a *= b:", a)  # Output: 10

a /= b  # a = a / b 
print("a /= b:", a)  # Output: 1.0

a //= b  # a = a // b
print("a //= b:", a)  # Output: 0.0

a %= b  # a = a % b
print("a %= b:", a)  # Output: 0.0

a **= b  # a = a ** b
print("a **= b:", a)  # Output: 0.0

# Membership operators are used to test if a sequence is present in an object. They return a boolean value (True or False) based on the membership. The membership operators are: in, not in.

fruits = ["apple", "banana", "cherry"]
print("apple in fruits:", "apple" in fruits)  # Output: True

# identity operators are used to compare the memory locations of two objects. They return a boolean value (True or False) based on the identity. The identity operators are: is, is not.

x = [1, 2, 3]
y = [1, 2, 3]
print("x is y:", x is y)  # Output: False
print("x is not y:", x is not y)  # Output: True