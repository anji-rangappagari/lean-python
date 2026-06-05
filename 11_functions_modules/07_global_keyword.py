def modify_global_variable():
    global global_variable  # declaring that we want to use the global variable global_variable
    global_variable = "Modified value"  # modifying the value of the global variable global_variable   

global_variable = "Initial value"  # defining a global variable global_variable and assigning it the value "Initial value"
print(global_variable)  # Initial value  # printing the value of the global variable global_variable
modify_global_variable()  # calling the function to modify the global variable
print(global_variable)  # Modified value  # printing the modified value of the global variable global_variable


def sum(a, b):
    global result  # declaring that we want to use the global variable result
    result = a + b  # modifying the value of the global variable result by assigning it the sum of a and b
    return result  # returning the value of result
print(sum(2, 3))  # 5  # calling the sum function with arguments 2 and 3 and printing the result
print(result)  # 5  # printing the value of the global variable result which is


#  excess of using global variable is that it can lead to unexpected behavior and bugs in the code because global variables can be modified from anywhere in the code, which can make it difficult to track changes and debug issues. It can also make the code less modular and harder to maintain because it creates dependencies between different parts of the code. It can also lead to naming conflicts if multiple functions or modules use the same global variable name, which can cause unintended consequences. Therefore, it is generally recommended to avoid using global variables whenever possible and instead use function parameters and return values to pass data between functions.