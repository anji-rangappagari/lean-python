
try:
    
    a = input("enter first number: ")
    b = input("enter second number: ")

    print("The sum of the two numbers is: ", int(a) + int(b))

    o = input("enter the operator: ")

    match o:
        case "+":
            print(f"The sum of the two numbers is: {int(a) + int(b)}")
        case "-":
            print(f"The difference of the two numbers is: {int(a) - int(b)}")
        case "*":
            print(f"The product of the two numbers is: {int(a) * int(b)}")
        case "/":
            print(f"The quotient of the two numbers is: {int(a) / int(b)}")
        case _:
            print("Invalid operator")
    b
except Exception as e:
    print("An error occurred: ",  a and b)

