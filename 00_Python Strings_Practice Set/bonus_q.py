# 6. Bonus Questions
# Write a program that counts how many vowels are in a given string.
# # Take a user input string and check if it is a palindrome (same forwards and backwards).

str1 = "I am Anji ,age is 25 and learning python programming"
vowels = "aeiouAEIOU"
count = 0
for char in str1:
    if char in vowels:
        count += 1
print(f"Number of vowels in the string: {count}")  # Number of vowels in the string: 16