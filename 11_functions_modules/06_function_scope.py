def sum(a, b): # a and b are the local variables of the function sum, they are only accessible inside the function sum and they are not accessible outside the function sum. They are created when the function is called and they are destroyed when the function is executed. They are stored in the memory until the function is executed and once the function is executed they are deleted from the memory. This is called function scope.
    c = a + b 
    return c

print(sum(2, 3))  # 5  # calling the sum function with arguments 2 and 3 and printing the result

# functions keeps variables until it return once its retunrs its wioeed out of the function scope we cannot access the variable c because it is defined inside the function sum and it is not accessible outside the function. This is called function scope. That its delete from the memory once the function is executed and it is not accessible outside the function. This is why we cannot access the variable c outside the function sum. If we try to access the variable c outside the function sum, we will get a NameError because the variable c is not defined in the global scope.