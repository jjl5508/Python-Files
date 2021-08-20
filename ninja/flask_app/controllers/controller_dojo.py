from flask import render_template, redirect, request
from flask_app.models.models_dojo import Dojo
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app 

@app.route("/dojo")
def dojo():
    all_dojos = Dojo.get_all()
    return render_template('dojo.html', all_dojos = all_dojos)

@app.route('/dojo_show/<dojo_id>')
def dojo_show(dojo_id):
    data = {"id":dojo_id}
    this_dojo = Dojo.get_one(data)
    return render_template('dojo_show.html', this_dojo = this_dojo)

@app.route("/dojos/<int:id>/ninja", methods = ['POST'])
def add_ninja(id):
    query = "INSERT INTO ninjas (dojo_id) VALUES %(dojo_id)%"
    data = {"dojo_id":id}
    connectToMySQL("ninja_schema").query_db(query,data)
    return redirect (f"dojo/{id}")

@app.route("/")
def new():
    return redirect ("/dojo")