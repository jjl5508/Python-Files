from flask import render_template, redirect, request
from flask_app.models.models_author import Author
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app
@app.route("/authors") 
def authors():
    #get all authors and pass to template
    all_authors = Author.get_all()
    return render_template('authors.html', all_authors = all_authors)

@app.route("/authors/<int:id>")
def authors_show(id):
    #get one author and pass it to template
    data = {"id":id}
    author = Author.get_one(data)
    return render_template('authors_show.html', author = author)

@app.route("/authors/create" , methods =['POST'])
def create_author():
    #create an author based on the for data
    Author.create(request.form)
    return redirect("/authors")

@app.route("/authors/<int:id>/favorite-book" , methods = ['POST'])
def add_book(id):
    #add a book to author based on form data
    query = "INSERT INTO favorites(author_id, book_id) VALUES (%(author_id)s , %(book_id)s)"
    data = {"author_id":id , "book_id":request.form["book_id"]}
    connectToMySQL("books_schema").query_db(query,data)
    return redirect(f"authors/{id}")
