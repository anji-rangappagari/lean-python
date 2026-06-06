# Constructor and Attributes

# 2. Constructor and Attributes
# Create a class Person with a constructor (__init__) that accepts name and age as arguments and stores them as instance attributes.
# Create an object and print the person’s name and age.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

person = Person("Alice", 30)
person.display_info()  # Output: Name: Alice, Age: 30
