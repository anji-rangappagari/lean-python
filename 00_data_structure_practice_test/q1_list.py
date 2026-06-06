# 1 Introduction to Lists
# Create a list fruits = ["apple", "banana", "cherry"] .
# Print the first fruit.
# Replace "banana" with "orange" .
# Print the length of the list.
# Create a list of numbers from 1 to 10 .
# Print the first three numbers using slicing.
# Print the last three numbers using slicing


# 1 Introduction to Lists

fruits = ["apple", "banana", "cherry"]
print(fruits[0])
fruits[1] = "orange"
print(len(fruits))

numbers = list(range(1, 11))
print(numbers[:3])
print(numbers[-3:])