from flask import render_template
from myapp import app


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/react')
def react():
    return render_template('react.html')