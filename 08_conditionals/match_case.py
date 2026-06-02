# match case statement is a conditional statement that allows us to execute a block of code based on the value of a variable. It is similar to the switch case statement in other programming languages. The syntax of a match case statement is as follows:

a = int(input("Enter a number between 1 and 10: "))

match a:
    case 1:
        print("You won camera 1.")
    case 2:
        print("You won Apple Studio 10.")
    case 3:
        print("You won House Studio 8.")
    
    case _:
        print("Next time better luck.")