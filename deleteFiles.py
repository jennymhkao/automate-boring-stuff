# !/usr/bin/env python3
# deleteFiles.py - deletes unneeded files. 

import os
# only if truly deleting - import shutil, send2trash 

# Ask what directory to search.
search_dir = input('What directory do you want me to search?')
root = os.path.abspath(search_dir)

if not os.path.exists(root):
    print("Provide valid source folder")
else:
    # Walks through folder tree using os.listdir().
    for filename in os.listdir(root):
        filepath = os.path.join(root, filename)

        # Get file size
        size = 0
        size += os.path.getsize(filepath)

    


    