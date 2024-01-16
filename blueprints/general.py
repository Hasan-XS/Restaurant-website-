from flask import Blueprint

app = Blueprint("general",__name__)

@app.route("/")
def home():
    return "home"

@app.route("/menu")
def menu():
    return "menu"

@app.route("/about")
def about():
    return "about"