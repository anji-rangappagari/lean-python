# . Creating Command Line Utilities
# Write a small script count_lines.py that takes a filename as input and prints how many lines are in the file.Example usage:

# python count_lines.py tasks.txt
# # Output: Number of lines: 4
 
 

# Write a command-line utility search_word.py that takes two arguments:

# A filename
# A word to search and prints how many times the word appears in the file.

# Example usage:

import orgparse
# python search_word.py tasks.txt Python
# # Output: The word 'Python' appears 3 times in the file.
parser = orgparse.Parser()
parser.add_argument("filename", help="The name of the file to search")
parser.add_argument("word", help="The word to search for")
args = parser.parse_args()
filename = args.filename
word = args.word    
with open(filename, 'r') as file:
    content = file.read()
    word_count = content.count(word)
    print(f"The word '{word}' appears {word_count} times in the file.")
    
