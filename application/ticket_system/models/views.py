from flask import jsonify
from .models import Ticket, Comment, User
from .serializers import TicketSerializer, CommentSerializer, UserSerializer


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


def get():
    users = User.query.all()
    serializer = UserSerializer(users, many=True)
    return jsonify(serializer.data)


class UserListView:
    pass


def get(user_id):
    user = User.query.get_or_404(user_id)
    serializer = UserSerializer(user)
    return jsonify(serializer.data)


class UserDetailView:
    pass
