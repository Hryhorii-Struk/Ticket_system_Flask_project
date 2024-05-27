from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class AdminModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    profile_id = db.Column(db.Integer, db.ForeignKey('profiles.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    profile = db.relationship('ProfileModel', backref='admin')
    user = db.relationship('UserModel', backref='admin')


class ProfileModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # Add profile fields here


class UserModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # Add user fields here


# Create the Flask app and configure the database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'your-database-uri'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# Create the database tables
with app.app_context():
    db.create_all()

# Run the Flask app
if __name__ == '__main__':
    app.run()