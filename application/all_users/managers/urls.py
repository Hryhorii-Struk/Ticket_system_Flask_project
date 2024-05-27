from importlib.resources import Resource

from flask import Flask

from flask import jsonify

from flask_sqlalchemy import SQLAlchemy

from application.ticket_system.auth.views import Api

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'your_database_uri'
db = SQLAlchemy(app)
api = Api(app)

class ManagerModel(db.Model):
    __tablename__ = 'manager'
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=db.func.now())
    updated_at = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now())

    def __repr__(self):
        return f'<ManagerModel(id={self.id})>'

class BanUserView(Resource):
    def post(self, pk):
        manager = ManagerModel.query.get(pk)
        if manager:
            # Perform ban user logic here
            return jsonify({'message': 'User banned successfully'}), 200
        else:
            return jsonify({'message': 'Manager not found'}), 404

class UnBanUserView(Resource):
    def post(self, pk):
        manager = ManagerModel.query.get(pk)
        if manager:
            # Perform unban user logic here
            return jsonify({'message': 'User unbanned successfully'}), 200
        else:
            return jsonify({'message': 'Manager not found'}), 404

api.add_resource(BanUserView, '/<int:pk>/ban_user')
api.add_resource(UnBanUserView, '/<int:pk>/un_ban_user')

if __name__ == '__main__':
    db.create_all()
    app.run()
