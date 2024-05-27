from flask import Blueprint
from . import views

analysts_blueprint = Blueprint('analysts', __name__)


@analysts_blueprint.route('/tickets', methods=['GET'])
def get_tickets():
    return views.get_tickets()


@analysts_blueprint.route('/tickets', methods=['POST'])
def create_ticket():
    return views.create_ticket()


@analysts_blueprint.route('/tickets/<int:ticket_id>', methods=['GET'])
def get_ticket(ticket_id):
    return views.get_ticket(ticket_id)


@analysts_blueprint.route('/tickets/<int:ticket_id>', methods=['PUT'])
def update_ticket(ticket_id):
    return views.update_ticket(ticket_id)


@analysts_blueprint.route('/tickets/<int:ticket_id>', methods=['DELETE'])
def delete_ticket(ticket_id):
    return views.delete_ticket(ticket_id)
