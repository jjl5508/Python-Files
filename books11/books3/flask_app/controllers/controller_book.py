from flask_app import app
from flask import render_template, request , redirect
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.models_books import Book


@app.route("/books")
def books():
    #get all books and pass to template
    all_books = Book.get_all()
    return render_template('books.html', all_books = all_books)

@app.route("/books/<int:id>")
def books_show(id):
    #get one book and pass it to template
    data= {"id":id}
    book = Book.get_one(data)
    return render_template('books_show.html', book = book)

@app.route("/books/create" , methods =['POST'])
def create_book():
    #create  book based on the for data
    Book.create(request.form)
    return redirect("/books")

@app.route("/books/<int:id>/favorite-author" , methods = ['POST'])
def favorite_author(id):
    #add a book to book based on form data
    query ="INSERT INTO favorites (author_id, book_id) VALUES (%(author_id)s , %(book_id)s)"
    data = {"author_id":request.form["author_id"] , "book_id":id}
    connectToMySQL("books_schema").query_db(query, data)
    return redirect(f"books/{id}")
