"""local.py
View development on local server before deployment
"""

from os.path import abspath, dirname

from jinja2 import FileSystemLoader
from flask import Flask, render_template

app = Flask(__name__)
app.jinja_loader = FileSystemLoader(dirname(abspath(__file__)))


@app.route('/')
def home():
    """Returns home"""
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
