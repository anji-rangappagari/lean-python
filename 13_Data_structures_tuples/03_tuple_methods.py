# tuple methods
# tuples have only two built-in methods: count() and index().       

# why use tuples
# tuples are used when you want to store a collection of items that should not change throughout the program. They are immutable, which means their elements cannot be modified after creation. This makes tuples useful for fixed data, such as coordinates, RGB values, or any other data that should remain constant.

# faster than lists (since they are immutable, they can be optimized by Python's internal implementation), and they can be used as keys in dictionaries (since they are hashable), while lists cannot.

# used as dictionary keys (since they are hashable)
# set from unintended duplicate modifications (since they are immutable)

t = (1, 2, 3, 2, 4, 2)
print(t.count(2))  # Output: 3 // The count() method returns the number of times a specified value appears in the tuple.
print(t.index(2))  # Output: 1  // The index() method returns the index of the first occurrence of the specified value. If the value is not found, it raises a ValueError.


# tuples do not have methods for adding, removing, or changing elements because they are immutable. However, you can concatenate tuples to create a new tuple:
t1 = (1, 2, 3)

