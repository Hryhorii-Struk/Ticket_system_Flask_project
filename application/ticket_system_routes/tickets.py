from flask import Blueprint, render_template
from flask_login import login_required

from application.ticket_system_admin.models.ticket import Ticket

tickets_bp = Blueprint('tickets', __name__)


@tickets_bp.route('/tickets', methods=['GET'])
@login_required
def tickets():
    tickets = Ticket.query.all()
    return render_template('tickets.html', tickets=tickets)


@tickets_bp.route('/tickets/<int:ticket_id>', methods=['GET'])
@login_required
def ticket(ticket_id):
    ticket = Ticket.query.get(ticket_id)
    return render_template('ticket.html', ticket=ticket)
