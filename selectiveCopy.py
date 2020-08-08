#! python3
'''selectiveCopy.py - A program that walks through a folder tree and 
searches for files with a certain file extension (such as .pdf or .jpg). 
Copy these files from whatever location they are in to a new folder.
'''

import os, shutil

# Ask what extension to look for
extension = input('What file extension should I copy?')

# Ask what folder to copy files to, and TODO: create it if it doesn't exist.
copy_dir = input('What directory am I copying to?')
copy_dir_abs = os.path.abspath(copy_dir)

# Ask what directory to search
search_dir = input('What directory do you want me to search?')
search_dir_abs = os.path.abspath(search_dir)

def selectiveCopy(folder, destination):
    # Walks through folder tree using os.walk(folder).
    for foldername, filenames in os.walk(search_dir_abs):
        print('Searching files in %s...' % (foldername))
        for filename in filenames:
            # Search for files with file extension .pdf.
            if filename.endswith('.%s' % extension):
                print('Copying %s from %s to %s...' % (filename, foldername, destination))
                shutil.copy(os.path.join(foldername, filename), copy_dir_abs)

print('Done')
