#3. Tuples and Operations on Tuples
# Create a tuple coordinates = (10, 20) and print both elements.
# Try to modify the tuple by setting coordinates[0] = 50 — note what
# happens.
# Convert the tuple to a list, change its first element to 50 , and convert it back
# to a tuple.

coordinates = (10, 20)
print(coordinates[0])  # Output: 10
print(coordinates[1])  # Output: 20

# Trying to modify the tuple (will raise an error)
# coordinates[0] = 50  # Uncommenting this line will raise a TypeError

# Convert the tuple to a list, modify it, and convert it back to a tuple
coordinates_list = list(coordinates)
coordinates_list[0] = 50
coordinates = tuple(coordinates_list)
print(coordinates)  # Output: (50, 20)