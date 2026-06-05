# defining a function
# def greet(name):
#     print(f"Hello, {name}!")
#     return "Greeting sent to " + name    

# greet("Anji")  # Hello, Anji!

# The below code works but it is not a good practice to use the same name for the function and the variable. It can lead to confusion and errors in the code. It is better to use different names for the function and the variable.
a = 1
b = 10
c = 100

d = (a + b + c) / 3
print(d)  # 37.0


# write a function that takes three numbers as input and returns the average of those numbers.
def average(a: float, b: float, c: float) -> float:
        d = (a + b + c) / 3
        return d
result = average(1111, 1011, 1001111)
print(result)  # 334411.0

result = average(12355111, 20000, 20000999)
print(result)  # 10852070.0

def greeting(name: str) -> str:
    return f"Hello, {name}!"

print(greeting("Anji"))  # Hello, Anji!
print(greeting("Ranga"))  # Hello, Ranga!




