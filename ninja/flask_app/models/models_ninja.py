from flask_app.config.mysqlconnection import connectToMySQL

class Ninja:
    def __init__(self, data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data ["last_name"]
        self.age = data ["age"]
        self.dojo_id = data ["dojo_id"]
        self.created_at = data ["created_at"]
        self.updated_at = data ["updated_at"]
    @classmethod
    def create(cls, data):
        # Adding a new item to the database returns that items id
        query = "INSERT INTO ninjas (first_name,last_name,age,dojo_id, created_at, updated_at) VALUES (%(first_name)s,%(last_name)s,%(age)s,%(dojo_id)s, NOW(), NOW());"
        return connectToMySQL("ninja_schema").query_db(query, data)
    @classmethod
    def get_all(cls):
        # Selecting all from the database returns a list of dictionary objects
        query = "SELECT * FROM  ninjas"
        results = connectToMySQL ("ninja_schema"). query_db(query)
        ninjas = []
        for result in results:
            ninjas.append(Ninja(result))
        return ninjas
    @classmethod
    def get_one(cls,data):
        # Selecting by ID will return a list with one object
        query = 'SELECT * FROM  ninja WHERE id = %(id)s'
        results = connectToMySQL ("ninja_schema"). query_db(query, data)
        return Ninja(results[0])
