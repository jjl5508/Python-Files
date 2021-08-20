from flask_app.models.models_ninja import Ninja
from flask import render_template, redirect, request
from flask_app.models.models_dojo import Dojo
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app 

@app.route('/dojo/create', methods=['POST'])
def create_dojo():
    data = {
        'name': request.form['name']
    }

    Dojo.create(data)

    return redirect("/dojo")

@app.route('/ninja/create', methods=['POST'])
def create_ninja():
    data = {
        'dojo_id': request.form['dojo_id'],
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'age': request.form['age'],
    }

    Ninja.create(data)
    redirecthere = "/dojo_show/"+ request.form['dojo_id']
    return redirect(redirecthere)

@app.route('/ninja/creates')
def creates_ninja():
    return render_template('ninja.html', all_dojos = Dojo.get_all())