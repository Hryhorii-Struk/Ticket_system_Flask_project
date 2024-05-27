from importlib.resources import Resource

from flask import Flask
from flask_pagedown import fields

from flask_sqlalchemy import SQLAlchemy

from application.all_users.admins.serializers import marshal_with

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'your_database_uri'
db = SQLAlchemy(app)


class ManagerModel(db.Model):
    __tablename__ = 'manager'
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=db.func.now())
    updated_at = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now())

    def __repr__(self):
        return f'<ManagerModel(id={self.id})>'


class ManagerSerializer(Resource):
    def get(self):
        manager = ManagerModel.query.first()
        if manager:
            result = {
                'id': manager.id
            }
            return result, 200
        else:
            return {'message': 'Manager not found'}, 404

    @marshal_with(fields.Integer(attribute='id'))
    def post(self):
        manager = ManagerModel(id=1)
        db.session.add(manager)
        db.session.commit()
        return manager, 201


if __name__ == '__main__':
    db.create_all()
    app.run()
