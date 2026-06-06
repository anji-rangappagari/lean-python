import pandas as pd

# Example of a simple if statement
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

# Example of a more complex if statement
temperature = 30
if temperature > 30:
    print("It's a hot day.")   
elif temperature > 20:
    print("It's a nice day.")   
else:
    print("It's a bit cold.")


read_csv = pd.read_csv("data.csv")