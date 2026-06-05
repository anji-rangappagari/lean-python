# dictionaries are a collection of key-value pairs
# they are unordered, mutable, and indexed by keys
# creating a dictionary
my_dict = { "name": "Anji", "age": 38, "city": "Hong Kong"}
print(my_dict)
print(my_dict["name"])  # accessing value by key
my_dict["age"] = 39  # updating value by key
print(my_dict)

# adding a new key-value pair
my_dict["email"] = "anji@example.com"
print(my_dict)