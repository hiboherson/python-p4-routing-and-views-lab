from flask import Flask, Response

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Python Operations with Flask Routing and Views</h1>"

@app.route('/print/<parameter>')
def print_string(parameter):
    print(parameter)
    return parameter

@app.route('/count/<int:parameter>')
def count(parameter):
    numbers = [str(i) for i in range(parameter)]
    return Response("\n".join(numbers) + "\n", mimetype='text/plain')

@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1, operation, num2):
    result = None
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/' or operation == 'div':
        if num2 == 0:
            return "Error: Division by zero", 400
        result = num1 / num2
    elif operation == '%':
        result = num1 % num2
    else:
        return "Error: Invalid operation", 400
    
    return str(result)

if __name__ == '__main__':
    app.run(port=5555, debug=True)
