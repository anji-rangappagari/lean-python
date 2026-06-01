# This loop will run infinitely until we say "break"
while True:
    try:
        age = int(input("Please enter your age: "))
        
        if age >= 18:
            print("Welcome in!")
        else:
            print("You are too young!")
            
        # This stops the loop because we got a valid number!
        break 
        
    except ValueError:
        # If an error happens, the code jumps straight here
        print("Invalid input! Let's try that again...")
        print("-----------------------------------")
        # Notice there is NO break here, so the loop starts over!

print("Program successfully completed and exited.")



