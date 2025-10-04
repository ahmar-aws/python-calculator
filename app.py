from flask import Flask, render_template, request

app = Flask(__name__, static_folder='static', template_folder='templates')


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    a = float(request.form['a'])
    b = float(request.form['b'])
    op = request.form['op']

    if op == '+': result = a + b
    elif op == '-': result = a - b
    elif op == '*': result = a * b
    elif op == '/': result = a / b if b != 0 else "Error: divide by zero"
    else: result = "Invalid operation"

    return render_template('result.html', result=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)

