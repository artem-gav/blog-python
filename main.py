from flask import Flask, request, render_template
from db import DB

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', request=request, data=DB.mycol.find())

@app.route('/user/<user>')
def user(user):
    return 'This %s user page' % user

@app.route('/post/<int:post_id>')
def post(post_id):
    return 'It\'s %s post' % post_id

if(__name__ == '__main__'):
    app.run()