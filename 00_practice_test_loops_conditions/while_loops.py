
# Print numbers from 1 to 10 using a while loop.
# Write a program that keeps asking the user to enter a password until they enter the correct one.
# Use a while loop to reverse a given number (e.g., 123 → 321).

# Print numbers from 1 to 10 using a while loop.
# i = 1
# while i <= 10:
#     print(i)
#     i += 1  
# print("Numbers from 1 to 10 have been printed.")

# # Write a program that keeps asking the user to enter a password until they enter the correct one.
# correct_password = "leanpython"
# user_password = ""
# while user_password != correct_password:
#     user_password = input("Enter the password: ")
# print("Password accepted.")

# Use a while loop to reverse a given number (e.g., 123 → 321).
number = int(input("Enter a number to reverse: "))
reversed_number = 0
while number > 0:
    digit = number % 10
    reversed_number = reversed_number * 10 + digit
    number //= 10
print(f"Reversed number: {reversed_number}")
