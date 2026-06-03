# string methods are built-in functions that can be used to manipulate and work with strings in Python. They allow you to perform various operations on strings, such as changing the case, replacing characters, splitting the string into a list, and more. Here are some commonly used string methods:
# 1. upper(): Converts all characters in the string to uppercase.
# 2. lower(): Converts all characters in the string to lowercase.
# 3. title(): Converts the first character of each word to uppercase and the rest to lowercase.
# 4. strip(): Removes any leading and trailing whitespace from the string.
# 5. replace(old, new): Replaces all occurrences of the old substring with the new substring.
# 6. split(separator): Splits the string into a list of substrings based on the specified separator.
# 7. join(iterable): Joins the elements of an iterable (like a list) into a single string, with the string as the separator.
# 8. find(substring): Returns the lowest index of the substring if it is found in the string, otherwise returns -1.
# 9. count(substring): Returns the number of occurrences of the substring in the string
#  strings are immutable, which means that once a string is created, it cannot be changed. However, you can create a new string by applying string methods to an existing string. For example:

# cannot change actual string in memory but we can create a new string by applying string methods to an existing string
# s = "Anjineyulu Rangappagari"
# a = len(s)
# print(a)
# print(s.upper())
# print(s.lower())


# # strip method removes any leading and trailing whitespace from the string
# s1 = "   Anjineyulu Rangappagari   "
# print(s1.strip())
# print(s1.lstrip())  # removes leading whitespace
# print(s1.rstrip())  # removes trailing whitespace

# find, replace, split, join
s2 = "Anjineyulu Rangappagari"
print(s2.find("Rangappagari"))  # returns the index of the first occurrence of the substring
print(s2.replace("Anjineyulu", "Anji"))  # replaces all occurrences of the old substring with the new substring
print(s2.split())  # splits the string into a list of substrings based on the specified separator (default is whitespace)
print("-".join(s2.split()))  # joins the elements of an iterable (like a list) into a single string, with the string as the separator
print(s2.count("a"))  # returns the number of occurrences of the substring in the string