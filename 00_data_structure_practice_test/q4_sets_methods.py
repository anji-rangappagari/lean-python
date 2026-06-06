# 4. Sets and Set Methods
# Create a set my_set = {1, 2, 3, 3, 4} and print it. (What happens to
# duplicate 3 ?)
# Add 5 to the set, remove 2 , and check if 4 is in the set.
# Create two sets:
# a = {1, 2, 3}
# b = {3, 4, 5}
# Find their:
# Union
# Intersection
# Difference ( a - b 


my_set = {1, 2, 3, 3, 4}
print(my_set)  # Output: {1, 2, 3, 4} (duplicate 3 is removed)

my_set.add(5)
print(my_set)  # Output: {1, 2, 3, 4, 5}

my_set.remove(2)
print(my_set)  # Output: {1, 3, 4, 5}

print(4 in my_set)  # Output: True

a = {1, 2, 3}
b = {3, 4, 5}

print(a.union(b))        # Output: {1, 2, 3, 4, 5}
print(a.intersection(b)) # Output: {3}
print(a.difference(b))   # Output: {1, 2}   