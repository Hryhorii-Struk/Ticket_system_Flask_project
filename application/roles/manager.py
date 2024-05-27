
from flask import render_template, Blueprint, redirect, url_for
from flask_login import login_required, current_user

from application.ticket_system.forms.models import Ticket

ticket_bp = Blueprint('ticket', __name__)


def has_analyst_or_manager_role():
    return current_user.role in ['analyst', 'manager']


@ticket_bp.route('/tickets', methods=['GET'])
@login_required
def tickets():
    if has_analyst_or_manager_role():
        group_id = current_user.group_id
        tickets = Ticket.query.filter_by(group_id=group_id).all()
        return render_template('tickets.html', tickets=tickets)
    else:
        tickets = Ticket.query.all()
        return render_template('tickets.html', tickets=tickets)


@ticket_bp.route('/tickets/<int:ticket_id>', methods=['GET'])
@login_required
def ticket(ticket_id):
    if has_analyst_or_manager_role():
        ticket = Ticket.query.get(ticket_id)
        if ticket.group_id != current_user.group_id:
            return redirect(url_for('ticket.tickets'))
        return render_template('ticket.html', ticket=ticket)
    else:
        ticket = Ticket.query.get(ticket_id)
        return render_template('ticket.html', ticket=ticket)
