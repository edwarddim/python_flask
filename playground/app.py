from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", num = 3, color="blue")

@app.route("/play/<int:num>")
def num(num):
    return render_template("index.html", num = num, color="blue")

@app.route("/play/<int:num>/<string:color>")
def color(num, color):
    return render_template("index.html", num = num, color=color)

if __name__ == "__main__":
    app.run(debug = True)