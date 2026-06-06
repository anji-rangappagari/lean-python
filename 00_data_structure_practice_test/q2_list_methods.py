# 2 List Methods
# Start with numbers = [5, 2, 9, 1, 7] and do the following:
# Sort the list in ascending order
# Add the number 10 to the end of the list
# Remove the number 2 from the list

#  create a list names = ["Alice", "Bob", "Charlie"] and do the following:
# Add the name "David" at index 1.


numbers = [5, 2, 9, 1, 7]

numbers.sort()
print(numbers)  # Output: [1, 2, 5, 7, 9]

numbers.append(10)
print(numbers)  # Output: [1, 2, 5, 7, 9, 10]

numbers.remove(2)
print(numbers)  # Output: [1, 5, 7, 9, 10]

# print(sorted(numbers))  # Output: [1, 2, 5, 7, 9]

names = ["Alice", "Bob", "Charlie"]
names.insert(1, "David")    
print(names)  # Output: ['Alice', 'David', 'Bob', 'Charlie']
