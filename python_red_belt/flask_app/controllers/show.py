from flask_app.models.shows import Shows
from flask import render_template, redirect, request, session
from flask_app.models.users import User
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app

@app.route('/shows/news', methods = ['POST'])
def create_show():
    if not Shows.validatecreate(request.form):
        return redirect('/shows/new')
    data = {
        'title': request.form['title'],
        'user_id':session['user_id'],
        'description': request.form['description'],
        'network': request.form['network'],
        'release_date': request.form['release_date']
    }

    Shows.create(data)
    return redirect("/dashboard")

@app.route('/shows/new')
def procreate():
    return render_template('show.html')

@app.route('/delete/<int:id>')
def delete(id):
    data = {
        'id':id
    }
    Shows.delete(data)
    return redirect('/dashboard')

@app.route('/edit/<int:id>')
def edit(id):
    data = {
        'id': id
    }
    results = Shows.get_one(data)
    print("((((((((((((((((((((")
    return render_template('edit.html', results = results)

@app.route('/edit/<int:id>', methods = ['POST'])
def edit_show(id):
    if not Shows.validatecreate(request.form):
        return redirect('/edit/%s'%(id))
    data = {
        'title': request.form['title'],
        'description': request.form['description'],
        'network': request.form['network'],
        'release_date': request.form['release_date'],
        'id': id
    }

    Shows.edit(data)
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
    shows_list = Shows.get_all()
    return render_template("dashboard.html", user = logged_in_user, shows_list = shows_list)

@app.route('/show/<int:id>')
def display(id):
    data = {
        'id':id
    }
    this_show = Shows.get_one(data)
    posted = User.get_user_by_id(data)
    print(posted,"please show yourself")
    return render_template('display.html', this_show = this_show, users = posted)

@app.route('/logout')
def logout():
    session.clear()

    return redirect('/')