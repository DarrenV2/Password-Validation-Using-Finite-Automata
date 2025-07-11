from naive import dfa_validate_password


userPassword = input ("Enter Password:")

if dfa_validate_password(userPassword):
    print('Password Accepted')
else:
    print('Password was rejected')