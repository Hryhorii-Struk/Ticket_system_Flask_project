from flask import Blueprint
from . import views

bp = Blueprint('ticket', __name__)

bp.add_url_rule('/tickets/', view_func=views.TicketList.as_view('ticket_list'))
bp.add_url_rule('/tickets/<int:ticket_id>/', view_func=views.TicketDetail.as_view('ticket_detail'))