from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    print("This is home!")
    return render_template("index.html", x = 8, y = 8, color1 = "#3333ff", color2 = "#f2f2f2")

@app.route('/<int:num>')
def new_page(num):
    return render_template('index.html', x = 8, y = num, color1 = "#ffffff", color2 = "#4d0066")

@app.route('/<int:x>/<int:y>')
def new_board(x,y):
    return render_template('index.html', x = x, y = y, color1 = "#ff471a", color2 = "#330a00")

@app.route('/<int:x>/<int:y>/<color1>/<color2>')
def cool_board(x,y,color1,color2):
    return render_template('index.html', x = x, y = y, color1 = color1, color2 = color2)


if __name__=="__main__":
    app.run(debug=True)