# 3. Lambda Functions
# Write a lambda function that adds two numbers and test it.
# Create a list [1, 2, 3, 4, 5] and use map() with a lambda function to get their squares.


# Lambda function to add two numbers
add = lambda a, b: a + b
# Testing the lambda function
result = add(10, 20)
print(result)  # This will print: 30

# Creating a list and using map() with a lambda function to get their squares
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x ** 2, numbers))
print(squares)  # This will print: [1, 4, 9, 16, 25]