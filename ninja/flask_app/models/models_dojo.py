from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import models_ninja

class Dojo:
    def __init__(self,data):
        self.id = data ['id']
        self.name = data ["name"]
        self.created_at = data ["created_at"]
        self.updated_at = data ["updated_at"]
        self.ninjas =[]
    @classmethod
    def create(cls, data):
        #query database to create dojo
        query = "INSERT INTO dojo (name) VALUES (%(name)s)"
        return connectToMySQL("ninja_schema").query_db(query, data)
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM  dojo"
        results = connectToMySQL ("ninja_schema"). query_db(query)
        dojo = []
        for result in results:
            dojo.append(Dojo(result))
        return dojo
    @classmethod
    def get_one(cls,data):
        query = 'SELECT * FROM  dojo JOIN ninjas ON ninjas.dojo_id = dojo.id WHERE dojo.id = %(id)s;'
        results = connectToMySQL ("ninja_schema"). query_db(query, data)
        dojos = cls(results[0])

        for row_from_db in results:
            ninja_data = {
                'id': row_from_db['ninjas.id'],
                'first_name': row_from_db['first_name'],
                'last_name': row_from_db['last_name'],
                'age':row_from_db['age'],
                'dojo_id':row_from_db['dojo_id'],
                'created_at': row_from_db['ninjas.created_at'],
                'updated_at': row_from_db['ninjas.updated_at']
                
            }
            dojos.ninjas.append(models_ninja.Ninja(ninja_data))
        return dojos
