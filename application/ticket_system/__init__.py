from flask import Flask
from flask_login import LoginManager
from flask_principal import Principal
from flask_sqlalchemy import SQLAlchemy

from config import Config

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
login_manager = LoginManager(app)
principal = Principal(app)

app.register_blueprint(url_prefix='/ticket')

if __name__ == '__main__':
    app.run()
