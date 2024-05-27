from importlib.resources import Resource

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class EmailSerializer(Resource):
    def __init__(self, reqparse=None):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('email', type=str, required=True)

    def post(self):
        args = self.parser.parse_args()
        email = args['email']
        # Perform serialization logic here
        return {'email': email}, 200


class PasswordSerializer(Resource):
    def __init__(self, reqparse=None):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('password', type=str, required=True)

    def post(self):
        args = self.parser.parse_args()
        password = args['password']
        # Perform serialization logic here
        return {'password': password}, 200