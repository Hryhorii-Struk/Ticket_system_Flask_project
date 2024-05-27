from flask import Flask
from .models import db
from .routes import user_bp

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db.init_app(app)

app.register_blueprint(user_bp)


class User:
    pass
