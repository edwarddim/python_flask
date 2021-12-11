from flask import Flask, render_template, redirect, request
from mysqlconnection import connectToMySQL
app = Flask(__name__)

@app.route("/")
def index():
    mysql = connectToMySQL('dojos_and_ninjas_schema')
    dojos = mysql.query_db('SELECT * FROM dojos;')
    return render_template("index.html", dojos = dojos)

@app.route("/dojos/create", methods = ['POST'])
def create():
    mysql = connectToMySQL('dojos_and_ninjas_schema')
    query = "INSERT INTO dojos  (name, created_at, updated_at) VALUES (%(name)s,NOW(), NOW());"
    data = {
        'name' : request.form['dojo']
    }
    new_dojo_id = mysql.query_db(query, data)
    print(new_dojo_id)
    return redirect('/')

@app.route("/ninjas")
def ninjas():
    mysql = connectToMySQL('dojos_and_ninjas_schema')
    dojos = mysql.query_db('SELECT * FROM dojos;')
    return render_template("new_ninja.html", dojos = dojos)

@app.route("/ninjas/new", methods = ['POST'])
def processNinja():
    mysql = connectToMySQL('dojos_and_ninjas_schema')
    query = "INSERT INTO ninjas (first_name, last_name, age, dojo_id ,created_at, updated_at) VALUES (%(f_name)s, %(l_name)s, %(age)s, %(dojo_id)s, NOW(), NOW());"
    data = {
        "f_name" : request.form['first_name'],
        "l_name" : request.form['last_name'],
        "age" : request.form['age'],
        "dojo_id" : request.form['dojo_id']
    }
    new_ninja_id = mysql.query_db(query, data)
    print(new_ninja_id)
    return redirect("/")



@app.route("/dojos/<int:dojo_id>")
def dojoShow(dojo_id):
    mysql = connectToMySQL('dojos_and_ninjas_schema')
    query = "SELECT ninjas.first_name, ninjas.last_name, dojos.name AS dojo_name FROM ninjas JOIN dojos ON dojos.id = ninjas.dojo_id WHERE dojos.id = %(dojo_id)s;"
    data = {
        'dojo_id' : dojo_id
    }
    ninjas = mysql.query_db(query, data)
    print(ninjas)
    return render_template("ninjas.html", ninjas = ninjas)

if __name__ == "__main__":
    app.run(debug=True)