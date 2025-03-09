from flask import Flask
from routes.contacts import contacts
from utils.db import db  

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:1234@localhost/contactsdb"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
app.register_blueprint(contacts)
