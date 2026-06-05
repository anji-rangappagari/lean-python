#  tuple and unpacking
# tuple packing and unpacking are powerful features in Python that allow you to assign multiple values to a single variable (packing) and then extract those values into separate variables (unpacking).

# tuple packing is the process of creating a tuple by grouping multiple values together. This can be done simply by separating

packed_tuple = 1, 2, 3
print(packed_tuple)  # Output: (1, 2, 3)

# tuple unpacking is the process of assigning the values from a tuple to individual variables. This can be done by matching the number of variables on the left side of the assignment with the number of elements in the tuple.
a, b, c = packed_tuple
print(a)  # Output: 1
print(b)  # Output: 2
print(c)  # Output: 3

print(a ,b ,c)  # Output: 1 2 3