# position arguments
def add(a, b): # a and b are the parameters
    x = a + b
    return x

c = add(10, 20)   # 10 and 20 are the position arguments
print(c)  # 30


#  default arguments
def add(a, b, plus=0): # a is a required parameter and b is an optional parameter with a default value of 10
    x = a + b + plus
    return x

c = add(10, 20, 2)   # 10 and 20 are the position arguments
print(c)  # 32


# keyword arguments
def add(a, b, plus=0): # a is a required parameter and b is an optional parameter with a default value of 10
    x = a + b + plus
    return x   
c = add(a=110, b=220, plus=22)   # 10 and 20 are the position arguments
print(c)  # 352