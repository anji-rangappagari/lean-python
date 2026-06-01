# Step 1: Read the user input and turn it into a number
age = int(input("Enter your age: "))

# Step 2: Check the IF and ELSE IF (elif) conditions
if age > 18:
    print("Welcome in! (You are over 18)")
elif age == 18:
    print("Welcome in! (You are exactly 18)")
else:
    print("You are too young!")

# Step 3: Exit the program
print("Program finished. Exiting...")
