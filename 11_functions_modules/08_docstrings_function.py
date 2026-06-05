def add(a, b):
    """
    This function takes two arguments, a and b, and returns their sum.

    Parameters:
    a (int or float): The first number.
    b (int or float): The second number.

    Returns:
    int or float: The sum of a and b.
    """
    c = a + b  # calculating the sum of a and b and storing it in the variable c
    return c  # returning the value of c which is the sum of a and b

# print(add(2, 3))  # 5  # calling the add function with arguments 2 and 3 and printing the result
print(add.__doc__)  # printing the docstring of the add function to understand what the function does and how to use it