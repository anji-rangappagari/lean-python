
# Write a program that takes a list of numbers and removes all duplicates using
# a set
# list_numbers = {1, 2, 3, 4, 5,3, 4, 5, 6, 7, 8, 9, 10}
# print(list_numbers)  # Output: {1, 2, 3, 4, 5, 6, 7, 8, 9, 10} (duplicates removed)

# Given a dictionary of products and their prices, find the product with the
# highest price.
products = {
    "Laptop": 1200,
    "Smartphone": 800,
    "Headphones": 150,
    "Monitor": 300
}

max_price = max(products.values())
for product, price in products.items():
    if price == max_price:
        print(f"The product with the highest price is {product} with a price of {price}.")


# Write a program that merges two dictionaries into one.
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
merged_dict = {**dict1, **dict2}
print(merged_dict)  # Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4}  