from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/dojo')
def dojo():
    return 'dojo'

@app.route('/say/<name>')
def say_name(name):
    return 'Hi, ' + name

@app.route('/repeat/<num>/<name>')
def repeat(num, name):
    return name * int(num)


if __name__ == "__main__":
    app.run(debug=True)