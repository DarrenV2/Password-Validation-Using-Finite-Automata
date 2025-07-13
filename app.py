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
    password = request.form['password']
    method = request.form['method']

    start_time = time.time()

    if method == 'dfa':
        dfa = DFA()
        is_valid = dfa.process_input(password)
    elif method == 'naive':
        is_valid = naive_validate_password(password)
    else:
        is_valid = False

    end_time = time.time()
    duration = round((end_time - start_time) * 1000, 4)  # Time in milliseconds

    result = "Valid" if is_valid else "Invalid"
    return render_template('result.html', result=result, method=method, duration=duration)


if __name__ == '__main__':
    app.run(debug=True)