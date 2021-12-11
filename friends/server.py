from flask import Flask, render_template, redirect, request
from mysqlconnection import connectToMySQL
app = Flask(__name__)

@app.route("/")
def index():
    mysql = connectToMySQL('friendships_schema')
    authors = mysql.query_db()
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)