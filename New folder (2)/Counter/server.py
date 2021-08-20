from flask import Flask, render_template, redirect, session 
app = Flask(__name__)
app.secret_key = 'pineapplejuice'

@app.route("/")
def counter():
    if 'count' not in session:
        session['count']=0
    session['count']+=1
    return render_template("index.html", count = session['count'])

@app.route("/destroy_session")
def reset():
    session['count']=0
    return redirect ('/')

if __name__=="__main__":
    app.run(debug=True)