# list comprehension
# list comprehension is a concise way to create lists



#  create list containing the table of 5.
# a = 5
# table = []
# for i in range(1, 11):
#     table.append(a * i)
# print(table)  # Output: [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
# list comprehension can be used to achieve the same result in a more concise way:
a = 5
table = [a * i for i in range(1, 11)]
print(table)  # Output: [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]

# Example: Create a list of squares of numbers from 1 to 5
squares = [x**2 for x in range(1, 6)]
print(squares)  # Output: [1, 4, 9, 16, 25]