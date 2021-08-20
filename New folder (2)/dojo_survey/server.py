from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/results', methods = ['POST'])
def create_response():
    print('Got Post Info')
    print(request.form)
    name_from_form = request.form['Full Name']
    email_from_form = request.form['email']
    location_from_form = request.form['Location']
    zip_from_form = request.form['Zip']
    city_from_form = request.form['City']
    language_from_form = request.form['Language']
    return render_template("show.html",city_on_template = city_from_form, name_on_template = name_from_form, email_on_template = email_from_form, location_on_template = location_from_form, zip_on_template = zip_from_form, language_on_template = language_from_form)



if __name__ =="__main__":
    app.run(debug=True)