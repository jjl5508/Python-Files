from flask_app.models.models_recipe import Recipe
from flask import render_template, redirect, request, session
from flask_app.models.user import User
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app
from datetime import date

@app.route('/recipes/news', methods = ['POST'])
def create_recipe():
    if not Recipe.validatecreate(request.form):
        return redirect('/recipes/new')
    data = {
        'name': request.form['name'],
        'user_id':session['user_id'],
        'description': request.form['description'],
        'instructions': request.form['instructions'],
        'time_limit': request.form['time_limit'],
        'date_made': request.form['date_made']
    }

    Recipe.create(data)
    return redirect("/dashboard")

@app.route('/recipes/new')
def procreate():
    return render_template('recipe.html')

@app.route('/delete/<int:id>')
def delete(id):
    data = {
        'id':id
    }
    Recipe.delete(data)
    return redirect('/dashboard')

@app.route('/edit/<int:id>')
def edit(id):
    data = {
        'id': id
    }
    results = Recipe.get_one(data)
    print("((((((((((((((((((((")
    return render_template('edit.html', results = results)

@app.route('/edit/<int:id>', methods = ['POST'])
def edit_recipe(id):
    if not Recipe.validatecreate(request.form):
        return redirect('/edit/%s'%(id))
    data = {
        'name': request.form['name'],
        'description': request.form['description'],
        'instructions': request.form['instructions'],
        'time_limit': request.form['time_limit'],
        'date_made': request.form['date_made'],
        'id': id
    }

    Recipe.edit(data)
    print("hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh")
    return redirect("/dashboard")

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect('/')
    data = {
        "id": session["user_id"]
    }

    logged_in_user = User.get_user_by_id(data)
    print(logged_in_user, "&&&&&&&&&&&&&&&")
    if logged_in_user == False:
        return redirect('/')
    recipes_list = Recipe.get_all()
    return render_template("dash.html", user = logged_in_user, recipes_list = recipes_list)

@app.route('/recipes/<int:id>')
def display(id):
    data = {
        'id':id
    }
    this_recipe = Recipe.get_one(data)
    return render_template('display.html', this_recipe = this_recipe)

@app.route('/logout')
def logout():
    session.clear()

    return redirect('/recipes')