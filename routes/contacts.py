from flask import Blueprint, render_template

contacts = Blueprint("Contacts", __name__)


@contacts.route("/")
def home():
    return render_template("index.html")


@contacts.route("/new")
def add():
    return render_template("new.html")


@contacts.route("/update")
def update():
    return "update contact"


@contacts.route("/delete")
def delete():
    return "delete contact"


@contacts.route("/about")
def about():
    return render_template("about.html")
