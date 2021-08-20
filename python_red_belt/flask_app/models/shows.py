from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import users
import re

LETTERS_ONLY_REGEX = re.compile(r"^[a-zA-Z]$")

class Shows:
    def __init__(self,data):
        self.id = data["id"]
        self.title = data["title"]
        self.description = data["description"]
        self.network = data["network"]
        self.user_id = data["user_id"]
        self.release_date = data["release_date"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.user = None
    @classmethod
    def create(cls,data):
        # Creating a new show
        query = "INSERT INTO shows (title,description,network,user_id, release_date, created_at,updated_at) VALUES (%(title)s, %(description)s, %(network)s, %(user_id)s, %(release_date)s, NOW(), NOW());"
        print(query)

        return connectToMySQL("show_schema"). query_db(query,data)

    @classmethod
    def add_likes(cls,data):
        query = "INSERT INTO likes (show_id, user_id) VALUES (%(id)s);"

        return connectToMySQL("show_schema").query_db(query,data)

    @classmethod
    def take_like(cls,data):
        query = "DELETE FROM likes WHERE %(id)s;"

        return connectToMySQL("show_schema").query_db(query, data)

    @classmethod
    def get_all(cls):
        # Selecting all shows from database and combine both tables
        query = "SELECT * FROM shows JOIN user ON shows.user_id = user.id;"
        results = connectToMySQL("show_schema").query_db(query)
        print(results,"@@@@@@@@@@@@@@@@@@@@@")
        shows = []
        for result in results:
            all_shows = cls(result)
            user_info = {
                "id":result["user.id"],
                "first_name":result['first_name'],
                "last_name":result['last_name'],
                "email":result['email'],
                "password":result['password'],
                "created_at":result['user.created_at'],
                "updated_at":result['user.updated_at']

            }
            all_shows.user = users.User(user_info)
            shows.append(all_shows)
        return shows

    @classmethod
    def get_one(cls,data):
        # Selecting one lucky show
        print("hello")
        query = "SELECT * FROM shows WHERE shows.id = %(id)s;"
        results = connectToMySQL("show_schema"). query_db(query,data)
        print(results)
        return cls(results[0])
        
    @classmethod
    def delete(cls, data):
        query = "DELETE FROM shows WHERE id = %(id)s;"

        connectToMySQL('show_schema').query_db(query, data)

    @classmethod
    def edit(cls, data):
        query = "UPDATE shows SET title = %(title)s, description = %(description)s, network = %(network)s, release_date = %(release_date)s WHERE id = %(id)s;"

        connectToMySQL('show_schema').query_db(query,data)


    @staticmethod
    def validatecreate(user):
        is_valid = True

        # Name
        if len(user['title']) == 0:
            flash("Title is required.", "title")
            is_valid = False
        # making sure its at least 3 letters
        elif len(user['title']) < 3:
            flash("Title must be at least 3 characters", "title")
            is_valid = False
        # letters only
        elif LETTERS_ONLY_REGEX.match(user['title']):
            flash("Title must not contain non-alphabetic characters.", "title")
            is_valid = False

        # Description
        if len(user['description']) == 0:
            flash("Description is required.", "description")
            is_valid = False
        # making sure its at least 3 letters
        elif len(user['description']) < 3:
            flash("Description must be at least 3 characters", "description")
            is_valid = False
        # letters only
        elif LETTERS_ONLY_REGEX.match(user['description']):
            flash("Description must not contain non-alphabetic characters.", "description")
            is_valid = False

        # Network
        if len(user['network']) == 0:
            flash("Network Name is required.", "network")
            is_valid = False
        # making sure its at least 3 letters
        elif len(user['network']) < 3:
            flash("Network Name must be at least 3 characters", "network")
            is_valid = False
        # letters only
        elif LETTERS_ONLY_REGEX.match(user['network']):
            flash("Network Name must not contain non-alphabetic characters.", "network")
            is_valid = False
        
        return is_valid
