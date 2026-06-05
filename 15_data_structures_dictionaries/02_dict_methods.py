# dict methods are built-in functions that can be used to manipulate dictionaries
my_dict = { "name": "Anji", "age": 38, "city": "Hong Kong"}

print(my_dict.keys())  # returns a view object of the keys in the dictionary
print(my_dict.values())  # returns a view object of the values in the dictionary
print(my_dict.items())  # returns a view object of the key-value pairs in the dictionary
print(my_dict.pop("age"))  # removes the key-value pair with the specified key and returns the value
print(my_dict)