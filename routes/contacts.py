from flask import Blueprint

contacts = Blueprint('Contacts',__name__)

@contacts.route("/")
def home():
    return "Contacts list"   

@contacts.route("/new")
def addContact():
    return "Saving a contact"   