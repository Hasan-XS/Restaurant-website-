from flask import Flask
from blueprints.admin import app as admin
from blueprints.general import app as general
import config

app = Flask(__name__)
app.config['SECRET_KEY'] = config.SECRET_KEY
app.register_blueprint(admin)
app.register_blueprint(general)


if __name__ == '__main__':
    app.run(debug=True)