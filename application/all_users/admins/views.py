from importlib.resources import Resource

from flask import Flask
from flask_pagedown import fields

from application.all_users.admins.models import UserModel
from application.all_users.admins.serializers import marshal_with
from application.ticket_system.auth.views import Api
from application.ticket_system.models.serializers import UserSerializer

app = Flask(__name__)


def jwt_required():
    pass


class IsSuperUser:
    pass


class UserToManagerView(Resource):
    @jwt_required
    @IsSuperUser.has_permission
    def patch(self, pk):
        user = UserModel.query.get_or_404(pk)
        if not user.is_staff:
            user.is_staff = True
            user.roles = 'manager'
            user.save()
        serializer = UserSerializer(user)
        return marshal_with(serializer.data, fields.Raw()), 200


class ManagerToUserView(Resource):
    @jwt_required
    @IsSuperUser.has_permission
    def patch(self, pk):
        user = UserModel.query.get_or_404(pk)
        if user.is_staff:
            user.is_staff = False
            user.roles = 'visitor'
            user.save()
        serializer = UserSerializer(user)
        return marshal_with(serializer.data, fields.Raw()), 200


class BanManagerView(Resource):
    serializer_class = UserSerializer

    @jwt_required
    @IsSuperUser.has_permission
    def patch(self, pk):
        user = UserModel.query.get_or_404(pk)
        if user.is_active:
            user.is_active = False
            user.roles = 'blocked'
            user.save()
        serializer = UserSerializer(user)
        return marshal_with(serializer.data, fields.Raw()), 200


class UnBanManagerView(Resource):
    serializer_class = UserSerializer

    @jwt_required
    @IsSuperUser.has_permission
    def patch(self, pk):
        user = UserModel.query.get_or_404(pk)
        if not user.is_active:
            user.is_active = True
            user.roles = 'manager'
            user.save()
        serializer = UserSerializer(user)
        return marshal_with(serializer.data, fields.Raw()), 200


# Register the API resources
api = Api(app)
api.add_resource(UserToManagerView, '/urls.py/<int:pk>/user_to_manager')
api.add_resource(ManagerToUserView, '/urls.py/<int:pk>/manager_to_user')
api.add_resource(BanManagerView, '/urls.py/<int:pk>/ban_manager')
api.add_resource(UnBanManagerView, '/urls.py/<int:pk>/un_ban_manager')

# Run the Flask app
if __name__ == '__main__':
    app.run()