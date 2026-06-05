# Write a function full_name(first, last) that takes first name and last name as parameters and returns a single string in the format "First Last".

# Write a function calculate_area(length, width=10) that returns the area of a rectangle. Test it by calling the function with:

# Both length and width
# Only length (use default width)


def full_name(first, last):
    return f"{first} {last}"

def calculate_area(length, width=10):
    return length * width

# Testing the functions
print(full_name("John", "Doe"))  # This will print: John Doe
print(calculate_area(5, 3))  # This will print: 15
print(calculate_area(5))  # This will print: 50 (using default width)