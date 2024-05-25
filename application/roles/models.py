from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    description = db.Column(db.String(128), nullable=True)

    def __repr__(self):
        return f"Role('{self.name}')"


class Group(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    description = db.Column(db.String(128), nullable=True)

    def __repr__(self):
        return f"Group('{self.name}')"
