from flask import Flask
from blueprints.admin import app as admin

app = Flask(__name__)

app.register_blueprint(admin)


if __name__ == '__main__':
    app.run(debug=True)