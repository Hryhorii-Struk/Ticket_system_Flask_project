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


class CommentListView:
    def get(self):
        comments = Comment.query.all()
        serializer = CommentSerializer(comments, many=True)
        return jsonify(serializer.data)


class CommentDetailView:
    def get(self, comment_id):
        comment = Comment.query.get_or_404(comment_id)
        serializer = CommentSerializer(comment)
        return jsonify(serializer.data)


class UserListView:
    def get(self):
        users = User.query.all()
        serializer = UserSerializer(users, many=True)
        return jsonify(serializer.data)


class UserDetailView:
    def get(self, user_id):
        user = User.query.get_or_404(user_id)
        serializer = UserSerializer(user)
        return jsonify(serializer.data)
