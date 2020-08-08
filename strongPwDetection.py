# !/usr/bin/env python3
# strongPwdDetection.py - Strong Password Detection.

'''Write a function that uses regular expressions 
to make sure the password string it is passed is strong. 
A strong password is defined as one that is at least eight 
characters long, contains both uppercase and lowercase characters, 
and has at least one digit. You may need to test the string against 
multiple regex patterns to validate its strength.'''

import re 

param = re.compile(r'(?=.*[a-z])(?=.*[A-Z])(?=(.*\d)).{8,}')

# user input pw
def userInputPassword():
    pw = input('Enter password: ')
    mo = param.search(pw)   
    if (not mo):
        print('''Make sure password has 8 characters, contains both uppercase and lower case, 
        and has at least one digit''')
        return False
    else:
        print("Super strong!")
        return True

userInputPassword()