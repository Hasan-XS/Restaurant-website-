from flask import Blueprint, render_template

app = Blueprint("admin",__name__)

@app.route("/admin/login")
def login():
    return render_template("admin/login.html")

@app.route("/admin/dashboard")
def dashboard():
    return render_template("admin/dashboard.html")