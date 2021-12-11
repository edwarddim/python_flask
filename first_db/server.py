from flask import Flask, render_template, redirect, request
from mysqlconnection import connectToMySQL    # import the function that will return an instance of a connection
app = Flask(__name__)

@app.route("/")
def index():
    mysql = connectToMySQL('first_flask')	        # call the function, passing in the name of our db
    friends = mysql.query_db('SELECT * FROM friends;')  # call the query_db function, pass in the query as a string
    # print(friends)
    return render_template("index.html", all_friends = friends)

@app.route("/users/new")
def create():
    return render_template("new_user.html")

@app.route("/users/create", methods = ['POST'])
def processCreate():
    mysql = connectToMySQL('first_flask')
    query = "INSERT INTO friends (first_name, last_name, occupation, created_at, updated_at) VALUES (%(fn)s,%(ln)s,%(occupation)s, NOW(), NOW());"
    data = {
        "fn" : request.form['first_name'],
        "ln" : request.form['last_name'],
        "occupation" : request.form['occupation']
    }
    new_friend_id = mysql.query_db(query, data)
    return redirect("/")

@app.route("/users/<int:user_id>")
def show(user_id):
    mysql = connectToMySQL('first_flask')
    query = "SELECT * FROM friends WHERE id = %(user_id)s;"
    data = {
        'user_id' : user_id
    }
    one_user = mysql.query_db(query, data)
    return render_template("user.html", user = one_user[0])

@app.route("/users/<int:user_id>/edit")
def edit(user_id):
    mysql = connectToMySQL('first_flask')
    query = "SELECT * FROM friends WHERE id = %(user_id)s;"
    data = {
        'user_id' : user_id
    }
    one_user = mysql.query_db(query, data)
    return render_template("edit.html", user = one_user[0])

@app.route("/users/<int:user_id>/update", methods = ['POST'])
def update(user_id):
    mysql = connectToMySQL('first_flask')
    query = "UPDATE friends SET first_name = %(f_name)s, last_name = %(l_name)s, occupation = %(occupation)s WHERE id = %(user_id)s;"
    data = {
        'user_id' : user_id,
        "f_name" : request.form['first_name'],
        "l_name" : request.form['last_name'],
        "occupation" : request.form['occupation']
    }
    mysql.query_db(query, data)
    return redirect("/")

@app.route("/users/<int:user_id>/delete")
def delete(user_id):
    mysql = connectToMySQL('first_flask')
    query = "DELETE FROM friends WHERE id = %(user_id)s;"
    data = {
        'user_id' : user_id
    }
    print(mysql.query_db(query, data))
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)