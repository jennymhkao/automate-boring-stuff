#! python3
# renameDates.py - Renames filenames with American MM-DD-YYYY date format to European DD-MM-YYYY.

import shutil, os, re

# Create a regex that matches files with American date format.
datePattern = re.compile(r"""^(.*?) # All text before the date.
((0|1)?\d) -                        # One or two digits for the month
((0|1|2|3)?\d) -                    # One or two digits for the day.
((19|20)\d\d)                       # Four digits for th year.
(.*?)$                              # All text after the date.
""", re.VERBOSE)

# TODO: Loop over the files in the working directory.
for amerFilename in os.listdir('.'):    
    mo = datePattern.search(amerFilename) 

# TODO: Skip files without a date.
if mo == None:
    continue

# TODO: Get the different parts of the filename.
beforePart = mo.group(1)    
monthPart  = mo.group(2)    
dayPart    = mo.group(4)    
yearPart   = mo.group(6)    
afterPart  = mo.group(8)

# TODO: Form the European-style filename.
euroFilename = beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart

# TODO: Get the full, absolute file paths.
absWorkingDir = os.path.abspath('.')    
amerFilename = os.path.join(absWorkingDir, amerFilename)    
euroFilename = os.path.join(absWorkingDir, euroFilename)

# TODO: Rename the files.
print('Renaming "%s" to "%s"...' % (amerFilename, euroFilename))
#shutil.move(amerFilename, euroFilename)   # uncomment after testing