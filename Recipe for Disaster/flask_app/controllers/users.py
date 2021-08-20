from flask_app import app
from flask import render_template, redirect, request, session
from flask_bcrypt import Bcrypt
from flask_app.models.user import User
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/register', methods = ['POST'])
def register():
    print(request.form['first_name'])
    if not User.validate_registration(request.form):
        return redirect('/')

    hashed_password = bcrypt.generate_password_hash(request.form['password'])
    print(hashed_password,"testhash")
    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"],
        "password": hashed_password,
        
    }

    session['user_id'] = User.save(data)
    return redirect('/dashboard')



@app.route('/login', methods=['POST'])
def login():
    login_validation = User.validate_login(request.form)
    # print(login_validation, "======")
    if not login_validation:
        redirect('/')
    print(request.form['password'], "////////////")
    if not bcrypt.check_password_hash(login_validation['password'],request.form['password']):
        flash("Invalid email/password", "login_email")
        return redirect("/")
    session['user_id'] = login_validation['id']
    return redirect('/dashboard')

# @app.route('/dashboard')
# def dashboard(user_id):
#     if 'user_id' not in session:
#         return redirect('/')
#     data = {
#         "id": session["user_id"]
#     }

#     logged_in_user = User.get_user_by_id(data)
#     print(logged_in_user, "&&&&&&&&&&&&&&&")
#     if logged_in_user == False:
#         return redirect('/')

#     data = {"id":user_id}
#     this_user = User.get_one(data)    

#     return render_template("dash.html", user = logged_in_user, this_user = this_user)

# @app.route('/logout')
# def logout():
#     session.clear()

#     return redirect('/')
