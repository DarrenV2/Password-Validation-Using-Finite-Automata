# Authors: Darren Drummond, Frederica Forbes , Justin Edwards & Rajaire Thomas
# Date: July 13, 2025
# DFA Password Validation

from flask import Flask, render_template, request
from naive import naive_validate_password
from dfa import DFA
import time 

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/validate', methods=['POST'])
def validate():
    """
    Validate a password using the specified method (DFA or naive) and measure performance.
    
    Returns:
        Flask response: Rendered result template with validation outcome and timing
    """
    # Extract password and validation method from form data
    password = request.form['password']
    method = request.form['method']

    # Start timing the validation process
    start_time = time.time()

    # Choose validation method based on user selection
    if method == 'dfa':
        # Use DFA-based validation
        dfa = DFA()
        is_valid = dfa.process_input(password)
    elif method == 'naive':
        # Use naive regex-based validation
        is_valid = naive_validate_password(password)
    else:
        # Invalid method selected
        is_valid = False

    # Calculate execution time in milliseconds
    end_time = time.time()
    duration = round((end_time - start_time) * 1000, 4)  # Time in milliseconds

    # Determine result string for display
    result = "Valid" if is_valid else "Invalid"
    
    # Render the result page with validation outcome and performance metrics
    return render_template('result.html', result=result, method=method, duration=duration)


if __name__ == '__main__':
    app.run(debug=True)