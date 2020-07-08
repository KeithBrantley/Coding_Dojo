from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def hello_world():
    return render_template('index.html', phrase="hello", times=5)

@app.route('/success')
def success():
    return 'success'

@app.route('/hello/<name>')
def hello(name):
    print(name)
    return 'Hello, ' + name

@app.route('/users/<username>/<id>')
def show_user_profile(username, id):
    print(username)
    print(id)
    return 'username: ' + username + ', id: ' + id

if __name__=="__main__":
    app.run(debug=True)