# !/usr/bin/env python3
# deleteFiles.py - deletes unneeded files. 

import os
# only if truly deleting - import send2trash 

# Ask what directory to search.
search_dir = input('What directory do you want me to search?')
root = os.path.abspath(search_dir)

pathList = {}

if not os.path.exists(root):
    print("Provide valid source folder")
else:
    # Walk through folder tree using os.listdir().
    for filename in os.listdir(root):
        filepath = os.path.join(root, filename)

        # Get file size
        pathSize = os.path.getsize(filepath)
        if pathSize < 100000000:
            continue
        os.send2trash(filepath)
        print('Deleting' + filename + '...')
    


    