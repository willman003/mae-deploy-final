import os
from flask import Flask


from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

import flask_login as login


app = Flask(__name__)
app.config['SECRET_KEY'] = "Impossible to guess"

#---CONFIG-----
app.config['DEBUG'] = False
app.config['TESTING'] = False
app.config['CSRF_ENABLED'] = True
app.config['DATABASE_FILE'] = 'du_lieu/ql_mae.db?check_same_thread=False'
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL') or 'sqlite:///du_lieu/ql_mae.db?check_same_thread=False'
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
db.init_app(app)

db.create_all()
migrate = Migrate(app,db)

login_manager = login.LoginManager()
login_manager.init_app(app)
import Mae.xu_ly.xu_ly_model
# import Mae.app_Web_ban_hang
import Mae.app_quan_ly
import Mae.app_admin

