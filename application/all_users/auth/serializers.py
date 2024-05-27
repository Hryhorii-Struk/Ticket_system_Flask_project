from importlib.resources import Resource

from flask import Flask
from flask_pagedown import fields

from application.all_users.admins.serializers import marshal_with
from application.ticket_system.auth.serializers import EmailSerializer, PasswordSerializer
from application.ticket_system.auth.views import Api, UserModel

app = Flask(__name__)


class UserModelResource(Resource):
    def get(self, user_id):
        user = UserModel.query.get(user_id)
        if user:
            return marshal_with(user, fields.Raw()), 200
        else:
            return {'message': 'User not found'}, 404

    def put(self, user_id, reqparse=None):
        parser = reqparse.RequestParser()
        parser.add_argument('email', type=str)
        parser.add_argument('password', type=str)
        args = parser.parse_args()

        user = UserModel.query.get(user_id)
        if user:
            if args['email']:
                user.email = args['email']
            if args['password']:
                user.password = args['password']
            user.save()
            return marshal_with(user, fields.Raw()), 200
        else:
            return {'message': 'User not found'}, 404


class EmailSerializerResource(Resource):
    def post(self, reqparse=None):
        parser = reqparse.RequestParser()
        parser.add_argument('email', type=str, required=True)
        args = parser.parse_args()

        serializer = EmailSerializer(data=args)
        if serializer.is_valid():
            serializer.validated_data['email']
            # Perform any additional logic with the email
            return {'message': 'Email validated successfully'}, 200
        else:
            return {'message': 'Invalid email'}, 400


def post(reqparse=None):
    parser = reqparse.RequestParser()
    parser.add_argument('password', type=str, required=True)
    args = parser.parse_args()

    serializer = PasswordSerializer(data=args)
    if serializer.is_valid():
        password = serializer.validated_data['password']
        # Perform any additional logic with the password
        return {'message': 'Password validated successfully'}, 200
    else:
        return {'message': 'Invalid password'}, 400


class PasswordSerializerResource(Resource):
    pass


# Register the API resources
api = Api(app)
api.add_resource(UserModelResource, '/urls.py/<int:user_id>')
api.add_resource(EmailSerializerResource, '/email')
api.add_resource(PasswordSerializerResource, '/password')

# Run the Flask app
if __name__ == '__main__':
    app.run()
