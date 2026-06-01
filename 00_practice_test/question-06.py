# Q6: Simple Calculator
# Write a program that:
# Takes two numbers as input from the user.
# Prints their sum, difference, product, and quotient.

num1 = int(input("Enter the first number: "))  # Take the first number as input and convert to integer
num2 = int(input("Enter the second number: "))  # Take the second number as input and convert to integer

print(f"Sum: {num1 + num2}")  # Print the sum of the two numbers
print(f"Difference: {num1 - num2}")  # Print the difference of the two numbers
print(f"Product: {num1 * num2}")  # Print the product of the two numbers
if num2 != 0:  # Check if the second number is not zero to avoid division by zero
   print(f"Quotient: {num1 / num2}")  # Print the quotient of the two numbers