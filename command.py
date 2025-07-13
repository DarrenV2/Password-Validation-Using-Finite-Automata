# Authors: Darren Drummond, Frederica Forbes , Justin Edwards & Rajaire Thomas
# Date: July 13, 2025
# DFA Password Validation

from naive import dfa_validate_password

#Test using Command Prompt
userPassword = input ("Enter Password:")

if dfa_validate_password(userPassword):
    print('Password Accepted')
else:
    print('Password was rejected')