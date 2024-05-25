from flask import jsonify
from .models import Ticket, Comment
from .serializers import TicketSerializer, CommentSerializer


def get():
    tickets = Ticket.query.all()
    serializer = TicketSerializer(tickets, many=True)
    return jsonify(serializer.data)


class TicketListView:
    pass


def get(ticket_id):
    ticket = Ticket.query.get_or_404(ticket_id)
    serializer = TicketSerializer(ticket)
    return jsonify(serializer.data)


class TicketDetailView:
    pass


def get():
    comments = Comment.query.all()
    serializer = CommentSerializer(comments, many=True)
    return jsonify(serializer.data)


class CommentListView:
    pass


def get(comment_id):
    comment = Comment.query.get_or_404(comment_id)
    serializer = CommentSerializer(comment)
    return jsonify(serializer.data)


class CommentDetailView:
    pass
