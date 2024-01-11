from flask import Blueprint

app = Blueprint("admin",__name__)

@app.route("/admin/login")
def login():
    return "admin login"

