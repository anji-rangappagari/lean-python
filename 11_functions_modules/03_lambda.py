# lambda functions are anonymous functions that can be defined in a single line of code. They are often used for short, simple functions that are not intended to be reused elsewhere in the code.

square = lambda x: x ** x

print(square(2))  # 4
print(square(3))  # 27  

add = lambda a, b: a + b
print(add(10, 20))  # 30