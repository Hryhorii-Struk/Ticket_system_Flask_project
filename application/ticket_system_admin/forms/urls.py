from flask import Blueprint
from . import views

bp = Blueprint('forms', __name__)

bp.add_url_rule('/ticket-forms/', view_func=views.TicketFormListView.as_view('ticket_form_list'))
bp.add_url_rule('/ticket-forms/<int:ticket_form_id>/', view_func=views.TicketFormDetailView.as_view('ticket_form_detail'))
bp.add_url_rule('/comment-forms/', view_func=views.CommentFormListView.as_view('comment_form_list'))
bp.add_url_rule('/comment-forms/<int:comment_form_id>/', view_func=views.CommentFormDetailView.as_view('comment_form_detail'))
bp.add_url_rule('/user-forms/', view_func=views.UserFormListView.as_view('user_form_list'))
bp.add_url_rule('/user-forms/<int:user_form_id>/', view_func=views.UserFormDetailView.as_view('user_form_detail'))