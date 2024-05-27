from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Ticket(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String, nullable=False)
    status = db.Column(db.String(20), nullable=False, default='new')

    def __repr__(self):
        return f'Ticket {self.title}'
