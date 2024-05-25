from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Ticket(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    priority = db.Column(db.String(10), nullable=False)
    status = db.Column(db.String(20), nullable=False, default='open')
    assigned_to_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    assigned_to = db.relationship('User', backref=db.backref('tickets', lazy=True))


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(500), nullable=False)
    ticket_id = db.Column(db.Integer, db.ForeignKey('ticket.id'))
    ticket = db.relationship('Ticket', backref=db.backref('comments', lazy=True))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', backref=db.backref('comments', lazy=True))


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
