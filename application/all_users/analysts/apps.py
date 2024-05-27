from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config.from_object('config')

    from .models import db
    db.init_app(app)

    from .views import analysts_blueprint
    app.register_blueprint(analysts_blueprint)

    return app
