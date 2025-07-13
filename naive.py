# Authors: Darren Drummond, Frederica Forbes , Justin Edwards & Rajaire Thomas
# Date: July 13, 2025
# DFA Password Validation


# DFA validation using naive approach
def naive_validate_password(password):
    state ='q1'
    validState = 'q15'
    if not password:
        return False
    
    alphabet = {'a', 'b', 'A', 'B', '0', '1'}

    for i, character in enumerate(password): #loops through each character in password or user input
        if character not in alphabet: 
            return False # Invalid character 
        

         # Transition Logic

        if state == 'q0': 
            if character in {'a', 'b', 'A', 'B', '0', '1'}:
                state = 'q0'
            else:
                return False 
            
        if  state == 'q1': # Check if current state is equal to 'q1'
            if character in {'1', '0'}: #If current character is any of the listed characters then update state 
                state = 'q0'
            elif character in {'a', 'b'}:
                state = 'q2'
            elif character in {'A', 'B'}:
                state = 'q8'
            else:
                return False # Return False if State receives invalid input
         
        if state == 'q2':  # Check if current state is equal to 'q2'
            if character in {'a', 'b'}:
                state = 'q4'
            elif character in {'0', '1'}: #If current character is any of the listed characters then update state 
                state = 'q5'
            elif character in {'A', 'B'}:
                state = 'q9'
            else:
                return False # Return False if State receives invalid input
        
        if state == 'q3':  # Check if current state is equal to 'q3'
            if character in {'a', 'b'}: 
                state = 'q3'
            elif character in {'A', 'B'}: #If current character is any of the listed characters then update state 
                state = 'q11'
            elif character in {'0', '1'}:
                state = 'q7'
            else: 
                return False # Return False if State receives invalid input
       
        
        if state == 'q4':  # Check if current state is equal to 'q4'
            if character in {'a', 'b'}: 
                state = 'q3'
            elif character in {'A', 'B'}:
                state = 'q13'
            elif character in {'0', '1'}:
                state = 'q6'
            else:
                return False
            
        if state == 'q5' :  # Check if current state is equal to 'q5'
            if character in {'0', '1', 'a', 'b'}:
                state = 'q6'
            elif character in {'A', 'B'}:
                state = 'q13'
            else: 
                return False # Return False if State receives invalid input

        if state == 'q6':  # Check if current state is equal to 'q6'
            if character in {'0', '1', 'a', 'b'}:
                state = 'q7'
            elif character in {'A', 'B'}:
                state = 'q14'
            else:
                return False
            
        if state == 'q7':  # Check if current state is equal to 'q7'
            if character in {'0', '1', 'a', 'b'}:
                state = 'q7'
            elif character in {'A', 'B'}:
                state = 'q15' 
            else:
                return False # Return False if State receives invalid input

        if state == 'q8':  # Check if current state is equal to 'q8'
            if character in {'a', 'b', 'A', 'B'}:
                state = 'q9'
            elif character in {'0', '1'}:
                state = 'q12'
            else: 
                return False

        if state == 'q9':  # Check if current state is equal to 'q9'
            if character in {'0', '1'}:
                state = 'q13'
            elif character in {'a', 'b', 'A', 'B'}: #If current character is any of the listed characters then update state 
                state = 'q10'
            else: 
                return False
            
        if state == 'q10':  # Check if current state is equal to 'q10'
            if character in {'0', '1'}:
                state = 'q14'
            elif character in {'a', 'b', 'A', 'B'}:
                state = 'q11'
            else:
                return False
            
        if state == 'q11':  # Check if current state is equal to 'q11'
            if character in {'a', 'b', 'A', 'B'}:
                state = 'q11'
            elif character in {'0', '1'}: #If current character is any of the listed characters then update state 
                state = 'q15'
            else:
                return False

        if state == 'q12':  # Check if current state is equal to 'q12'
            if character in {'0', '1', 'a', 'b', 'A', 'B'}:
                state = 'q13' #update state
            else:
                return False
        
        if state == 'q13':  # Check if current state is equal to 'q13'
            if character in {'0', '1', 'a', 'b', 'A', 'B'}:
                state = 'q14'
            else:
                return False
        
        if state == 'q14':  # Check if current state is equal to 'q14'
            if character in {'0', '1', 'a', 'b', 'A', 'B'}:
                state = 'q15'
            else:
                return False
            
        if state == 'q15':  # Check if current state is equal to 'q15'
            if character in {'0', '1', 'a', 'b', 'A', 'B'}:
                state = 'q15'
            else:
                return False

    return len(password) >= 5 and state in validState # Check if password length is greater than 5 and is in the valid(accepting) state
    # returns True or False
         
 


