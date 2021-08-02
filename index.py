from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')

def open_web():
    return render_template('index.html')

app.run(host='localhost', port=5000)