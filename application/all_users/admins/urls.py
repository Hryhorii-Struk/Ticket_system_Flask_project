from flask import Flask

from application.ticket_system.auth.views import Api

app = Flask(__name__)
api = Api(app)


class UserToManagerView:
    pass


api.add_resource(UserToManagerView, '/<int:pk>/user_to_manager')


class ManagerToUserView:
    pass


api.add_resource(ManagerToUserView, '/<int:pk>/manager_to_user')


class BanManagerView:
    pass


api.add_resource(BanManagerView, '/<int:pk>/ban_manager')


class UnBanManagerView:
    pass


api.add_resource(UnBanManagerView, '/<int:pk>/un_ban_manager')

# Run the Flask app
if __name__ == '__main__':
    app.run()