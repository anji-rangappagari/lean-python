# 1. Open the "Try" safety net
try:
    # Try to read the input and convert it to a number
    age = int(input("Enter your age: "))

    # If conversion works, check the conditions normally
    if age >= 18:
        print("Welcome in!")
    else:
        print("You are too young!")

# 2. Catch the error if they typed letters
except ValueError:
    print("Error: Please type a valid number, not words or letters!")

# 3. Exit safely
print("Program finished. Exiting...")
