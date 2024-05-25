from flask import Blueprint
from . import views

models_blueprint = Blueprint('models', __name__)

models_blueprint.add_url_rule('/tickets/', view_func=views.TicketListView.as_view('ticket_list'))
models_blueprint.add_url_rule('/tickets/<int:ticket_id>/', view_func=views.TicketDetailView.as_view('ticket_detail'))
models_blueprint.add_url_rule('/comments/', view_func=views.CommentListView.as_view('comment_list'))
models_blueprint.add_url_rule('/comments/<int:comment_id>/', view_func=views.CommentDetailView.as_view('comment_detail'))
models_blueprint.add_url_rule('/users/', view_func=views.UserListView.as_view('user_list'))
models_blueprint.add_url_rule('/users/<int:user_id>/', view_func=views.UserDetailView.as_view('user_detail'))