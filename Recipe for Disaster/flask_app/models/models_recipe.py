from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import user
import re

LETTERS_ONLY_REGEX = re.compile(r"^[a-zA-Z]$")

class Recipe:
    def __init__(self,data):
        self.id = data["id"]
        self.name = data["name"]
        self.description = data["description"]
        self.instructions = data["instructions"]
        self.user_id = data["user_id"]
        self.time_limit = data["time_limit"]
        self.date_made = data ["date_made"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.user = None
    @classmethod
    def create(cls,data):
        # Creating a new recipe
        query = "INSERT INTO recipes (name,description,instructions,user_id, time_limit, date_made, created_at,updated_at) VALUES (%(name)s, %(description)s, %(instructions)s, %(user_id)s, %(time_limit)s, %(date_made)s, NOW(), NOW())"
        print(query)

        return connectToMySQL("recipe_schema"). query_db(query,data)

    

    @classmethod
    def get_all(cls):
        # Selecting all recipes from database and combine both tables
        query = "SELECT * FROM recipes JOIN user ON recipes.user_id = user.id;"
        results = connectToMySQL("recipe_schema").query_db(query)
        print(results,"@@@@@@@@@@@@@@@@@@@@@")
        recipes = []
        for result in results:
            all_recipe = cls(result)
            user_info = {
                "id":result["user.id"],
                "first_name":result['first_name'],
                "last_name":result['last_name'],
                "email":result['email'],
                "password":result['password'],
                "created_at":result['user.created_at'],
                "updated_at":result['user.updated_at']

            }
            all_recipe.user = user.User(user_info)
            recipes.append(all_recipe)
        return recipes

    @classmethod
    def get_one(cls,data):
        # Selecting one lucky recipe
        print("hello")
        query = "SELECT * FROM recipes WHERE recipes.id = %(id)s;"
        results = connectToMySQL("recipe_schema"). query_db(query,data)
        print(results)
        return cls(results[0])
        
    @classmethod
    def delete(cls, data):
        query = "DELETE FROM recipes WHERE id = %(id)s;"

        connectToMySQL('recipe_schema').query_db(query, data)

    @classmethod
    def edit(cls, data):
        query = "UPDATE recipes SET name = %(name)s, description = %(description)s, instructions = %(instructions)s, time_limit = %(time_limit)s, date_made = %(date_made)s WHERE id = %(id)s;"

        connectToMySQL('recipe_schema').query_db(query,data)


    @staticmethod
    def validatecreate(user):
        is_valid = True

        # Name
        if len(user['name']) == 0:
            flash("Name is required.", "name")
            is_valid = False
        # making sure its at least 3 letters
        elif len(user['name']) < 3:
            flash("Name must be at least 3 characters", "name")
            is_valid = False
        # letters only
        elif LETTERS_ONLY_REGEX.match(user['name']):
            flash("Name must not contain non-alphabetic characters.", "name")
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
        elif LETTERS_ONLY_REGEX.match(user['name']):
            flash("Description must not contain non-alphabetic characters.", "description")
            is_valid = False

        # Instruction
        if len(user['instructions']) == 0:
            flash("Instruction is required.", "instructions")
            is_valid = False
        # making sure its at least 3 letters
        elif len(user['name']) < 3:
            flash("Instructions must be at least 3 characters", "instructions")
            is_valid = False
        # letters only
        elif LETTERS_ONLY_REGEX.match(user['instructions']):
            flash("Instructions must not contain non-alphabetic characters.", "instructions")
            is_valid = False
        
        return is_valid
