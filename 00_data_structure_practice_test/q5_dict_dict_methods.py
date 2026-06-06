# 5. Dictionaries and Dictionary Methods
# Create a dictionary student = {"name": "John", "age": 20, "grade": "A"}
# and:
# Print the value of "name" .
# Change "grade" to "A+" .
# Add a new key "city" with value "Delhi" .
# Create a dictionary of three friends and their phone numbers. Use:
# keys() to get all names
# values() to get all numbers
# items() to loop over key-value pairs and print them

student = {"name": "John", "age": 20, "grade": "A"}
print (student["name"])  # Output: John

student["grade"] = "A+"
print(student)  # Output: {'name': 'John', 'age': 20, 'grade': 'A+'}

student["city"] = "Delhi"
print(student)  # Output: {'name': 'John', 'age': 20, 'grade': 'A+', 'city': 'Delhi'}

friends = {"Alice": "12345", "Bob": "67890", "Charlie": "54321"}
print(friends.keys())   # Output: dict_keys(['Alice', 'Bob', 'Charlie'])
print(friends.values()) # Output: dict_values(['12345', '67890', '54321'])

for name, number in friends.items():
    print(f"{name}: {number}")