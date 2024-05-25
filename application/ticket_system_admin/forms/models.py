from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class TicketForm(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    priority = db.Column(db.String(10), nullable=False)
    status = db.Column(db.String(20), nullable=False, default='open')


class CommentForm(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(500), nullable=False)
    ticket_id = db.Column(db.Integer, db.ForeignKey('ticket_form.id'))
    ticket = db.relationship('TicketForm', backref=db.backref('comments', lazy=True))


class UserForm(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
