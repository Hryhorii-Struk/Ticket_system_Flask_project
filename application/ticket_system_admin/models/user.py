from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    role = db.Column(db.String(64), nullable=False)
    group_id = db.Column(db.Integer, db.ForeignKey('group.id'))
    group = db.relationship('Group', backref=db.backref('users', lazy=True))
