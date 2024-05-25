from flask import request, jsonify

from .serializers import TicketSerializer
from .models import Ticket, db


def post():
    data = request.get_json()
    serializer = TicketSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return jsonify(serializer.data), 201
    return jsonify({'error': 'invalid data'}), 400


def get():
    tickets = Ticket.query.all()
    serializer = TicketSerializer(tickets, many=True)
    return jsonify(serializer.data)


class TicketList:
    pass


def get(ticket_id):
    ticket = Ticket.query.get_or_404(ticket_id)
    serializer = TicketSerializer(ticket)
    return jsonify(serializer.data)


def put(ticket_id):
    ticket = Ticket.query.get_or_404(ticket_id)
    data = request.get_json()
    serializer = TicketSerializer(ticket, data=data)
    if serializer.is_valid():
        serializer.save()
        return jsonify(serializer.data)
    return jsonify({'error': 'invalid data'}), 400


def delete(ticket_id):
    ticket = Ticket.query.get_or_404(ticket_id)
    db.session.delete(ticket)
    db.session.commit()
    return '', 204


class TicketDetail:
    pass
