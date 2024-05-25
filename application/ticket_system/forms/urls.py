from flask import Blueprint
from . import views

forms_blueprint = Blueprint('forms', __name__)

forms_blueprint.add_url_rule('/tickets/', view_func=views.TicketListView.as_view('ticket_list'))
forms_blueprint.add_url_rule('/tickets/<int:ticket_id>/', view_func=views.TicketDetailView.as_view('ticket_detail'))
forms_blueprint.add_url_rule('/comments/', view_func=views.CommentListView.as_view('comment_list'))
forms_blueprint.add_url_rule('/comments/<int:comment_id>/', view_func=views.CommentDetailView.as_view('comment_detail'))