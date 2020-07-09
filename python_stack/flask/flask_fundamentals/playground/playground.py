from flask import Flask, render_template
app = Flask(__name__)
@app.route('/play')
def play():
    return render_template('index.html')

@app.route('/play/<num>')
def boxes(num):
    num = int(num)
    return render_template('boxes.html', num = num)

@app.route('/play/<num>/<color>')
def color(num, color):
    num = int(num)
    color = color
    return render_template('color.html', num = num, color = color)

if __name__ == "__main__":
    app.run(debug=True)