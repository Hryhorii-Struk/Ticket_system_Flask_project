from flask import Blueprint

from application.all_users.analysts.views import create, update, delete
from application.ticket_system_routes.main import index

users_blueprint = Blueprint('users', __name__)

users_blueprint.route('/', methods=['GET'])(index)
users_blueprint.route('/create', methods=['GET', 'POST'])(create)
users_blueprint.route('/<int:id>/update', methods=['GET', 'POST'])(update)
users_blueprint.route('/<int:id>/delete', methods=['POST'])(delete)