from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_bcrypt import Bcrypt
from flask_app import app
bcrypt = Bcrypt(app)
import re

LETTERS_ONLY_REGEX = re.compile(r"^[a-zA-Z]$")
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


class User:
    def __init__(self, data):
        self.id = data['id'],
        self.first_name = data['first_name'],
        self.last_name = data['last_name'],
        self.email = data['email'],
        self.password = data['password'],
        self.created_at = data['created_at'],
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls, data):
        query = "INSERT INTO user (first_name,last_name,email,password,created_at,updated_at) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s, NOW(), NOW());"

        return connectToMySQL('user_schema').query_db(query, data)

    @classmethod
    def no_email_exist(cls, email):
        query = "SELECT * FROM user WHERE email = %(email)s;"
        data = {'email':email}
        results = connectToMySQL('user_schema').query_db(query, data)
        return len(results) == 0

    @classmethod
    def get_user_by_id(cls,data):
        query = "SELECT * FROM user WHERE id = %(id)s;"
        results = connectToMySQL('user_schema').query_db(query,data)

        if len(results) > 0:
            return cls(results[0])
        else:
            return False

    @classmethod
    def get_user_email(cls,data):
        query = "SELECT * FROM user WHERE email = %(email)s;"
        results = connectToMySQL('user_schema').query_db(query,data)

        if len(results) == 0:
            return False
        else:
            return results[0]

    @staticmethod
    def validate_registration(user):
        is_valid = True

        # First name
        if len(user['first_name']) == 0:
            flash("First name is required.", "first_name")
            is_valid = False
        # making sure its at least 2 letters
        elif len(user['first_name']) < 2:
            flash("First name must be at least 2 characters", "first_name")
            is_valid = False
        # letters only
        elif LETTERS_ONLY_REGEX.match(user['first_name']):
            flash("First name must not contain non-alphabetic characters.", "first_name")
            is_valid = False

        # Last Name
        if len(user['last_name']) == 0:
            flash("Last name is required.", "last_name")
            is_valid = False
        # making sure its at least 2 letters
        elif len(user['last_name']) < 2:
            flash("Last name must be at least 2 characters", "last_name")
            is_valid = False
        # letters only
        elif LETTERS_ONLY_REGEX.match(user['last_name']):
            flash("Last name must not contain non-alphabetic characters.", "last_name")
            is_valid = False

        # Email
        if len(user['email']) == 0:
            flash("Email is required.", "email")
            is_valid = False
        # Valid Email
        elif not EMAIL_REGEX.match(user['email']):
            flash("Invalid email format. Must meet username@emaildomain.com format", "email")
            is_valid = False
        # email not existing in database
        elif not User.no_email_exist(user['email']):
            flash("A user with that email already exists", "email")
            is_valid = False

        # Password
        if len(user['password']) == 0:
            flash("Password is required.", "password")
            is_valid = False
        # At least 8 letters
        elif len(user['password']) < 8:
            flash("Password must be at least 8 characters.", "password")
            is_valid = False
        # Matches confirm password
        elif user['password'] != user['confirm_password']:
            flash("Password must match.", "password")
            is_valid = False

        return is_valid

    @staticmethod
    def validate_login(login_user):
        user_in_db = User.get_user_email(login_user)
        # print(user_in_db['password'], "+++++++++")

        if not user_in_db:
            flash("Invalid email/password","login_email")
            return False

        
        return user_in_db
