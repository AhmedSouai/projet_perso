# app/src/main.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello, World!"

@app.route('/multiply/<int:a>/<int:b>')
def multiply(a, b):
    return str(a * b)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)

