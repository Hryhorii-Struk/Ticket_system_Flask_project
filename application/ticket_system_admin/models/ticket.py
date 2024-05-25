from app import db


class Ticket(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), nullable=False)
    description = db.Column(db.String(256), nullable=False)
    status = db.Column(db.String(64), nullable=False, default='pending')
    group_id = db.Column(db.Integer, db.ForeignKey('group.id'))
    group = db.relationship('Group', backref=db.backref('tickets', lazy=True))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', backref=db.backref('tickets', lazy=True))
