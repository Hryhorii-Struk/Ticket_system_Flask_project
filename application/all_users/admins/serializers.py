from importlib.resources import Resource

from flask import Flask
from flask_pagedown import fields
from flask_sqlalchemy import SQLAlchemy

from application.ticket_system.auth.views import api

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'your-database-uri'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class AdminModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    profile_id = db.Column(db.Integer, db.ForeignKey('profiles.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('urls.py.id'), nullable=False)

    profile = db.relationship('ProfileModel', backref='admin')
    user = db.relationship('UserModel', backref='admin')


class ProfileModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # Add profile fields here


class UserModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # Add user fields here


def marshal_with(ManagerSerializer):
    pass


class ManagerResource(Resource):
    class ManagerSerializer:
        id = fields.Integer()
        users = fields.Nested('UserSerializer')
        profile = fields.Nested('ProfileSerializer')

    @marshal_with(ManagerSerializer)
    def get(self):
        admin = AdminModel.query.first()
        if admin:
            return {
                'id': admin.id,
                'urls.py': admin.user,
                'profile': admin.profile
            }
        return {'message': 'Admin not found'}, 404


# Create the Flask app and configure the database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'your-database-uri'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# Create the database tables
with app.app_context():
    db.create_all()

# Register the API resources
api.add_resource(ManagerResource, '/manager')

# Run the Flask app
if __name__ == '__main__':
    app.run()