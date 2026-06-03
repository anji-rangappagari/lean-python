# Take the string "  i love python programming  " and:

# Remove extra spaces from both ends
# Convert it to title case
# Count how many times "o" appears
# Check if the string "123abc" is alphanumeric.



text = "  i love python programming  "
text = text.strip()
text = text.title()
o_count = text.count("O")
is_alphanumeric = "123abc".isalnum()

print(text)  # I Love Python Programming
print(o_count)  # 2
print(is_alphanumeric)  # True