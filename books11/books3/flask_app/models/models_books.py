from flask_app.config.mysqlconnection import connectToMySQL

class Book:
    def __init__(self, data):
        self.id = data["id"]
        self.title = data["title"]
        self.num_of_pages = data ["num_of_pages"]
        self.created_at = data ["self_created_at"]
        self.updated_at = data ["updated_at"]
    @classmethod
    def create(cls, data):
        #query database to create book
        query = "INSERT INTO books (title, num_of_pages) VALUES (%(title)s,%(num_of_pages)s)"
        return connectToMySQL("books_schema").query.db(query, data)
    @classmethod
    def get_all(cls):
        #query database to get all authors
        query = "SELECT * FROM  books"
        results = connectToMySQL ("books_schema"). query_db(query)
        books = []
        for result in results:
            books.append(Book(result))
        return books
    @classmethod
    def get_one(cls,data):
        query = 'SELECT * FROM  books WHERE id = %(id)s'
        results = connectToMySQL ("books_schema"). query_db(query, data)
        return Book(results[0])