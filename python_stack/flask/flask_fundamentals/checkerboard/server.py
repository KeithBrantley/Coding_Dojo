from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<x>')
def custom(x):
    x = int(x)
    return render_template('custom.html', x = x)

if __name__ == "__main__":
    app.run(debug=True)