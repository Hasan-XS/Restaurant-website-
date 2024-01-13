from flask import Blueprint, render_template, session, request,abort, redirect
import config
from Model.food import Food

app = Blueprint("admin",__name__)

@app.before_request
def before_request():
    if session.get('admin_login', None) == None and request.endpoint != "admin.login":
        abort(403)

# admin login routes
@app.route('/admin/login', methods=["POST", "GET"])
def login():
    if request.method == "POST":
        username = request.form.get('username', None)
        password = request.form.get('password', None)

        if username == config.ADMIN_LOGIN_USERNAME and password == config.ADMIN_LOGIN_PASSWORD:
            session['admin_login'] = username
            return redirect("/admin/dashboard")
        else:
            return redirect("/admin/login")

    else:
        return render_template("admin/login.html")
    
# admin add food
@app.route("/admin/food")
def food():
    return render_template("admin/food.html")


# admin dashboard routes
@app.route("/admin/dashboard", methods=["GET"])
def dashboard():
    return render_template("admin/dashboard.html")