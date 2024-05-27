from flask import Blueprint, Flask

from application import db
from application.all_users.users import routes

auth_bp = Blueprint('auth', __name__)

# Import the routes from the auth module


# Register the routes with the blueprint
auth_bp.add_url_rule('/login', view_func=routes.login, methods=['POST'])
auth_bp.add_url_rule('/register', view_func=routes.register, methods=['POST'])
auth_bp.add_url_rule('/verify-email/<token>', view_func=routes.verify_email, methods=['POST'])
auth_bp.add_url_rule('/forgot-password', view_func=routes.forgot_password, methods=['POST'])
auth_bp.add_url_rule('/reset-password/<token>', view_func=routes.reset_password, methods=['POST'])


# Register the blueprint with the Flask app
def create_app():
    app = Flask(__name__)
    app.register_blueprint(auth_bp, url_prefix='/auth')
    return app


# Create the Flask app and configure the database
app = create_app()
db.init_app(app)

# Run the Flask app
if __name__ == '__main__':
    app.run()
