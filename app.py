from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'This is my first project'


@app.route('/about')
def about():
    return 'This is a about page'