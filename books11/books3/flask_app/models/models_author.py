from flask_app.config.mysqlconnection import connectToMySQL

class Author:
    def __init__(self,data):
        self.id = data ['id']
        self.name = data ["name"]
        self.created_at = data ["created_at"]
        self.updated_at = data ["updated_at"]
    @classmethod
    def create(cls, data):
        #query database to create author
        query = "INSERT INTO authors (name) VALUES (%(name)s)"
        return connectToMySQL("books_schema").query.db(query, data)
    @classmethod
    def get_all(cls):
        #query database to get all authors
        query = "SELECT * FROM  authors"
        results = connectToMySQL ("books_schema"). query_db(query)
        authors = []
        for result in results:
            authors.append(Author(result))
        return authors
    @classmethod
    def get_one(cls,data):
        query = 'SELECT * FROM  authors WHERE id = %(id)s'
        results = connectToMySQL ("books_schema"). query_db(query, data)
        return Author(results[0])