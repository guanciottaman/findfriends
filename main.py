from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scroll')
def scroll():
    return render_template('scroll.html')

app.run(debug=True)