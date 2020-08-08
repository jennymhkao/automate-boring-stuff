# !/usr/bin/env python3
# madlibs.py - A program to let users set their own text anywhere if the word
# is ADJECTIVE, NOUN, ADVERB, or VERB. 

import re

# Define regex
check = re.compile(r'ADJECTIVE|NOUN|VERB|ADVERB')

# Open text file and save string to variable.
file_name = input("Enter the full name of the text file: ")
madlibs = open(file_name, 'r')
content = madlibs.read()
madlibs.close()

# match regex.
while True:
    match = check.search(content)

    if match is None:
        print('No matches left, saving final text file:\n\n')
        break
    # Get user input as soon as regex is match.
    else:
        replace = input(f"Enter a(n) %s: " % match.group().lower())
    # Replace the words
    content = content[:match.span()[0]] + replace + content[match.span()[1]:]

# Print output.    
print(content)

# Save output to file.
print("Name your file: ")
name = input()
new_file = open(".\\%s.txt" % (name), "w")
new_file.write(content)
new_file.close()


    
    

    






