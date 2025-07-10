def dfa_validate_password(password):
    state ='q1'
    validState = 'q15'
    if not password:
        return False
    
    alphabet = {'a', 'b', 'A', 'B', '0', '1'}

    for i, character in enumerate(password):
        if character not in alphabet: 
            return False # Invalid character 
        

         # Transition Logic

        if state == 'q0':
            if character in {'a', 'b', 'A', 'B', '0', '1'}:
                state = 'q0'
            else:
                return False
            
        if  state == 'q1':
            if character in {'1', '0'}:
                state = 'q0'
            elif character in {'a', 'b'}:
                state = 'q2'
            elif character in {'A', 'B'}:
                state = 'q8'
            else:
                return False
         
        if state == 'q2':
            if character in {'a', 'b'}:
                state = 'q4'
            elif character in {'0', '1'}:
                state = 'q5'
            elif character in {'A', 'B'}:
                state = 'q9'
            else:
                return False
        
        if state == 'q3':
            if character in {'a', 'b'}: 
                state = 'q3'
            elif character in {'A', 'B'}:
                state = 'q11'
            elif character in {'0', '1'}:
                state = 'q7'
            else: 
                return False
       
        
        if state == 'q4':
            if character in {'a', 'b'}: 
                state = 'q3'
            elif character in {'A', 'B'}:
                state = 'q13'
            elif character in {'0', '1'}:
                state = 'q6'
            else:
                return False
            
        if state == 'q5' :
            if character in {'0', '1', 'a', 'b'}:
                state = 'q6'
            elif character in {'A', 'B'}:
                state = 'q13'
            else: 
                return False

        if state == 'q6':
            if character in {'0', '1', 'a', 'b'}:
                state = 'q7'
            elif character in {'A', 'B'}:
                state = 'q14'
            else:
                return False
            
        if state == 'q7':
            if character in {'0', '1', 'a', 'b'}:
                state = 'q7'
            elif character in {'A', 'B'}:
                state = 'q15'
            else:
                return False

        if state == 'q8':
            if character in {'a', 'b', 'A', 'B'}:
                state = 'q9'
            elif character in {'0', '1'}:
                state = 'q12'
            else: 
                return False

        if state == 'q9': 
            if character in {'0', '1'}:
                state = 'q13'
            elif character in {'a', 'b', 'A', 'B'}:
                state = 'q10'
            else: 
                return False
            
        if state == 'q10':
            if character in {'0', '1'}:
                state = 'q14'
            elif character in {'a', 'b', 'A', 'B'}:
                state = 'q11'
            else:
                return False
            
        if state == 'q11':
            if character in {'a', 'b', 'A', 'B'}:
                state = 'q11'
            elif character in {'0', '1'}:
                state = 'q15'
            else:
                return False

        if state == 'q12':
            if character in {'0', '1', 'a', 'b', 'A', 'B'}:
                state = 'q13'
            else:
                return False
        
        if state == 'q13':
            if character in {'0', '1', 'a', 'b', 'A', 'B'}:
                state = 'q14'
            else:
                return False
        
        if state == 'q14':
            if character in {'0', '1', 'a', 'b', 'A', 'B'}:
                state = 'q15'
            else:
                return False
            
        if state == 'q15':
            if character in {'0', '1', 'a', 'b', 'A', 'B'}:
                state = 'q15'
            else:
                return False

    return len(password) >= 5 and state in validState
         
 


