#  Defining Functions
# Write a function greet() that prints "Hello, Python Learner!" when called.
# Write a function square(num) that returns the square of a given number. Test it with different numbers

def greet():
    print("Hello, Python Learner!")

def square(num):
    return num ** 2
# Testing the functions
greet()  # This will print: Hello, Python Learner!
print(square(4))  # This will print: 16


def add(a, b):
    c = a + b
    return c
# Testing the add function
result = add(5, 3)
print(result)  # This will print: 8