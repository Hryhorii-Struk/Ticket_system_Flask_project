from flask import Flask

from application.ticket_system.auth.views import Api
from .views import ActivateUserView, MeView, RecoveryPasswordRequest, RecoveryPasswordView

app = Flask(__name__)
api = Api(app)

api.add_resource(ActivateUserView, '/activate/<string:token>')
api.add_resource(RecoveryPasswordRequest, '/recovery_password')
api.add_resource(RecoveryPasswordView, '/recovery_password/<string:token>')
api.add_resource(MeView, '/me')

# Run the Flask app
if __name__ == '__main__':
    app.run()