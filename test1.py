from flask import Flask, redirect, url_for, render_template, session
app = Flask(__name__)

@app.route('/hello/')
def hello_world():
   return('Hello World')

@app.route('/python')
def python_on():
    return('welcome to python')

@app.route('/user/<name>')
def hello_user(name):
   if name =='admin':
      return redirect(url_for('python_on'))

@app.route('/lulu/<name>')
def hello_name(name):
    return 'hello {}'.format(name)
@app.route('/')
def index():
   return render_template('index.html')



if __name__=="__main__":
          app.run()