from importlib.resources import Resource
from urllib import request

from flask import Flask

from application.ticket_system.auth.serializers import EmailSerializer, PasswordSerializer
from application.ticket_system.auth.views import Api, JWTService, ActivateToken, UserModel, EmailService, RecoveryToken
from application.ticket_system.models.serializers import UserSerializer

app = Flask(__name__)
api = Api(app)


class MeView(Resource):
    def get(self):
        user = request.user
        serializer = UserSerializer(user)
        return {'data': serializer.data}, 200


class ActivateUserView(Resource):
    def post(self, token):
        user = JWTService.validate_token(token, ActivateToken)
        user.is_active = True
        user.save()
        serializer = UserSerializer(user)
        return {'data': serializer.data}, 200


class RecoveryPasswordRequest(Resource):
    def post(self):
        data = request.json
        serializer = EmailSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        user = UserModel.objects.get(**serializer.data)
        EmailService.recovery_password(user)
        return {'message': 'Check your email to reset your password'}, 200


class RecoveryPasswordView(Resource):
    def post(self, token):
        data = request.json
        serializer = PasswordSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        user = JWTService.validate_token(token, RecoveryToken)
        user.set_password(serializer.data['password'])
        user.save()
        return {'message': 'Password changed'}, 200


class ProfileSerializer:
    pass


class UpdateUserProfileView(Resource):
    def patch(self, user_id):
        user = UserModel.objects.get(id=user_id)
        data = request.json
        serializer = ProfileSerializer(user.profile, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=user)
        serializer = UserSerializer(user)
        return {'data': serializer.data}, 200


api.add_resource(MeView, '/me')
api.add_resource(ActivateUserView, '/activate/<string:token>')
api.add_resource(RecoveryPasswordRequest, '/recovery_password')
api.add_resource(RecoveryPasswordView, '/recovery_password/<string:token>')
api.add_resource(UpdateUserProfileView, '/urls.py/<int:user_id>')

if __name__ == '__main__':
    app.run()
