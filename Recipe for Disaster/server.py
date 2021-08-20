from flask_app import app
from flask_app.controllers import users, controller_recipe


if __name__ =='__main__':
    app.run(debug=True)