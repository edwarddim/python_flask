from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World"

@app.route("/dojo")
def dojo():
    return "Dojo!!"

@app.route("/say/<string:name>")
def name(name):
    return f"Hi {name}"

@app.route("/repeat/<int:num>/<string:name>")
def repeast(num, name):
    returnString = f"{name} " * int(num)
    return returnString

@app.route('/<path:path>')
def catch_all(path):
    return f"Oops looks like {path} doesn't exist"

if __name__ == "__main__":
    app.run(debug = True)