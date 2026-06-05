# data structures: lists
# lists are ordered, mutable, collection of items and allow duplicate elements
# creating a list
#  list can contain elements of different data types
marks = [85, 90, 78, 92, 88]
mixed_list = [1, "hello", 3.14, True]

print(marks)  # Output: [85, 90, 78, 92, 88]
print(mixed_list)  # Output: [1, 'hello', 3.14, True]
print(marks[0])  # Output: 85
print(mixed_list[1:3])  # Output: ['hello', 3.14] slicing
print(marks[-1])  # Output: 88
print(marks[::2])  # Output: [85, 78, 88]
print(mixed_list[4])  # Error IndexError: list index out of range