from flask import Flask, render_template, request
from main import dfa_validate_password
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/check', methods=['POST'])
def validate():
    password = request.form['password']
   
    result = "Valid" if dfa_validate_password(password) else "Invalid"
    return render_template('result.html', result=result)


   
if __name__ == '__main__':
    app.run(debug=True)