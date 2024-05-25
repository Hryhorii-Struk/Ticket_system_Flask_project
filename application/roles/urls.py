from flask import Blueprint
from . import views

roles_blueprint = Blueprint('roles', __name__)

roles_blueprint.add_url_rule('/roles/', view_func=views.RoleListView.as_view('role_list'))
roles_blueprint.add_url_rule('/roles/<int:role_id>/', view_func=views.RoleDetailView.as_view('role_detail'))
roles_blueprint.add_url_rule('/groups/', view_func=views.GroupListView.as_view('group_list'))
roles_blueprint.add_url_rule('/groups/<int:group_id>/', view_func=views.GroupDetailView.as_view('group_detail'))