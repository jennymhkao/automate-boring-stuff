#! python3
# bulletPointAdder.py - add star bullet point and space at beginning of each line.

import pyperclip
text = pyperclip.paste()

newText = text.split('\n')

for i in range(len(newText)):  # loop through all indexes in the "newText" list
    newText[i] = '* ' + newText[i] # add star to each string in "newText" list
new = '\n'.join(newText)

pyperclip.copy(text)