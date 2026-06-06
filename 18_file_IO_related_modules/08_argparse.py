# purpose of using ythe argeparse module is to create a simple calculator program that can perform basic arithmetic operations (addition, subtraction, multiplication, and division) on two numbers provided as command-line arguments. The argparse module allows us to easily parse and handle these command-line arguments, making our program more user-friendly and flexible.

import argparse

parser = argparse.ArgumentParser(description="Simple Calculator Program" \
"This program performs basic arithmetic operations on two numbers.")
parser.add_argument("num1", type=float, help="First number")
parser.add_argument("num2", type=float, help="Second number")
parser.add_argument("operation", choices=["add", "subtract", "multiply", "divide"], help="Arithmetic operation to perform")

args = parser.parse_args()

if args.operation == "add":
    result = args.num1 + args.num2  # This performs the math
    print(f"Result = {result}")     # This prints the final number

elif args.operation == "subtract":
    result = args.num1 - args.num2  # This performs the math
    print(f"Result = {result}")     # This prints the final number

elif args.operation == "multiply":
    result = args.num1 * args.num2  # This performs the math
    print(f"Result = {result}")     # This prints the final number

elif args.operation == "divide":
    if args.num2 != 0:
        result = args.num1 / args.num2  # This performs the math
        print(f"Result = {result}")     # This prints the final number
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operation")



