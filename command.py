# Authors: Darren Drummond, Frederica Forbes , Justin Edwards & Rajaire Thomas
# Date: July 13, 2025
# DFA Password Validation

# Usage: Run this script to quickly test password validation at the command line.
#        Users can choose between Naive and DFA validation methods.


from naive import naive_validate_password
from dfa import DFA

def main():
    """Simple command-line password validator"""
    print("=== Password Validator ===\n")
    
    # Choose validation method
    print("Choose validation method:")
    print("1. Naive (Regex)")
    print("2. DFA")
    
    while True:
        choice = input("\nEnter choice (1 or 2): ").strip()
        if choice in ['1', '2']:
            break
        print("Invalid choice. Please enter 1 or 2.")
    
    # Get password
    password = input("\nEnter password: ")
    
    # Validate based on choice
    if choice == '1':
        print("\nUsing Naive validation...")
        is_valid = naive_validate_password(password)
    else:
        print("\nUsing DFA validation...")
        dfa = DFA()
        is_valid = dfa.process_input(password)
    
    # Show result
    result = "ACCEPTED" if is_valid else "REJECTED"
    print(f"\nPassword: {result}")

if __name__ == "__main__":
    main()