from importlib.resources import Resource
from urllib import request

from flask import Flask, jsonify

from application.ticket_system.models.serializers import UserSerializer

app = Flask(__name__)


class Api:
    def add_resource(self, ManagerToUserView, param):
        pass


api = Api(app)


class MeView(Resource):
    def get(self):
        user = request.user
        serializer = UserSerializer(user)
        return jsonify(serializer.data), 200


class JWTService:
    pass


class ActivateToken:
    pass


class ActivateUserView(Resource):
    def post(self, token):
        user = JWTService.validate_token(token, ActivateToken)
        user.is_active = True
        user.save()
        serializer = UserSerializer(user)
        return jsonify(serializer.data), 200


class UserModel:
    query = None


class EmailService:
    pass


class RecoveryPasswordRequest(Resource):
    def post(self, reqparse=None):
        parser = reqparse.RequestParser()
        parser.add_argument('email', type=str, required=True)
        args = parser.parse_args()
        email = args['email']
        user = UserModel.query.filter_by(email=email).first()
        if user:
            EmailService.recovery_password(user)
            return jsonify('Check your email to reset your password'), 200
        else:
            return jsonify('User not found'), 404


class RecoveryToken:
    pass


class RecoveryPasswordView(Resource):
    def post(self, token, reqparse=None):
        parser = reqparse.RequestParser()
        parser.add_argument('password', type=str, required=True)
        args = parser.parse_args()
        password = args['password']
        user = JWTService.validate_token(token, RecoveryToken)
        user.set_password(password)
        user.save()
        return jsonify('Password changed'), 200


class UpdateUserProfileView(Resource):
    def patch(self, user_id, reqparse=None):
        user = UserModel.query.get(user_id)
        if user:
            parser = reqparse.RequestParser()
            parser.add_argument('name', type=str)
            parser.add_argument('age', type=int)
            args = parser.parse_args()
            user.profile.name = args['name']
            user.profile.age = args['age']
            user.profile.save()
            serializer = UserSerializer(user)
            return jsonify(serializer.data), 200
        else:
            return jsonify('User not found'), 404


api.add_resource(MeView, '/me')
api.add_resource(ActivateUserView, '/activate/<token>')
api.add_resource(RecoveryPasswordRequest, '/recovery-password')
api.add_resource(RecoveryPasswordView, '/recovery-password/<token>')
api.add_resource(UpdateUserProfileView, '/users/<int:user_id>/profile')

if __name__ == '__main__':
    app.run()