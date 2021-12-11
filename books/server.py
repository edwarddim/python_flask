from flask import Flask, render_template, redirect, request
from mysqlconnection import connectToMySQL
app = Flask(__name__)

@app.route("/")
def index():
    mysql = connectToMySQL('books_schema')
    authors = mysql.query_db("SELECT * FROM authors;")
    return render_template("index.html", authors = authors)

@app.route("/authors/create", methods = ['POST'])
def createAuthor():
    mysql = connectToMySQL('books_schema')
    query = "INSERT INTO authors (name, created_at, updated_at) VALUES (%(name)s, NOW(), NOW());"
    data = {
        'name': request.form['author']
    }
    new_author_id = mysql.query_db(query, data)
    print(new_author_id)
    return redirect("/")

@app.route("/authors/<int:author_id>")
def showAuthor(author_id):
    # ----------------------------------------------------#
    # QUERY TO GET FAVES FOR A SPECFIC AUTHOR
    mysql = connectToMySQL('books_schema')
    query = "SELECT books.title, books.num_of_pages, authors.name FROM authors JOIN favorites ON authors.id = favorites.author_id JOIN books ON books.id = favorites.book_id WHERE authors.id = %(author_id)s;"
    data = {
        'author_id' : author_id
    }
    faves = mysql.query_db(query, data)
    # ----------------------------------------------------#

    # ----------------------------------------------------#
    # QUERY TO GET SPECFIC AUTHOR INFO
    mysql = connectToMySQL('books_schema')
    query = "SELECT authors.name, authors.id FROM authors WHERE authors.id = %(author_id)s;"
    data = {
        'author_id' : author_id
    }
    author = mysql.query_db(query, data)
    # ----------------------------------------------------#

    # ----------------------------------------------------#
    # QUERY TO GET BOOKS NOT FAVORITED BY AUTHOR
    mysql = connectToMySQL('books_schema')
    query = "SELECT books.title, books.id FROM books WHERE books.id NOT IN (SELECT favorites.book_id FROM favorites WHERE favorites.author_id = %(author_id)s);"
    data = {
        'author_id' : author_id
    }
    exclude_books = mysql.query_db(query, data)
    # ----------------------------------------------------#

    return render_template("authors.html", faves = faves, books = exclude_books, author = author[0])

@app.route("/authors/favorites", methods = ['POST'])
def authorFaves():
    mysql = connectToMySQL('books_schema')
    query = "INSERT INTO favorites (author_id, book_id) VALUES (%(author_id)s, %(book_id)s);"
    data = {
        "author_id" : request.form['author_id'],
        "book_id" : request.form['book_id']
    }
    mysql.query_db(query, data)
    return redirect(f"/authors/{request.form['author_id']}")

@app.route("/books/new")
def newBook():
    mysql = connectToMySQL('books_schema')
    books = mysql.query_db("SELECT * FROM books;")
    return render_template("books.html", books = books)

@app.route("/books/create", methods = ['POST'])
def createBook():
    mysql = connectToMySQL('books_schema')
    query = "INSERT INTO books (title, num_of_pages,created_at, updated_at) VALUES (%(title)s, %(pages)s, NOW(), NOW());"
    data = {
        "title" : request.form['title'],
        "pages" : request.form['pages']
    }
    new_book_id = mysql.query_db(query, data)
    print(new_book_id)
    return redirect("/books/new")

if __name__ == "__main__":
    app.run(debug=True)