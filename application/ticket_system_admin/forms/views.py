from flask import  jsonify
from .models import TicketForm, CommentForm, UserForm
from .serializers import TicketFormSerializer, CommentFormSerializer, UserFormSerializer


class TicketFormListView:
    def get(self):
        ticket_forms = TicketForm.query.all()
        serializer = TicketFormSerializer(ticket_forms, many=True)
        return jsonify(serializer.data)


class TicketFormDetailView:
    def get(self, ticket_form_id):
        ticket_form = TicketForm.query.get_or_404(ticket_form_id)
        serializer = TicketFormSerializer(ticket_form)
        return jsonify(serializer.data)


class CommentFormListView:
    def get(self):
        comment_forms = CommentForm.query.all()
        serializer = CommentFormSerializer(comment_forms, many=True)
        return jsonify(serializer.data)


class CommentFormDetailView:
    def get(self, comment_form_id):
        comment_form = CommentForm.query.get_or_404(comment_form_id)
        serializer = CommentFormSerializer(comment_form)
        return jsonify(serializer.data)


class UserFormListView:
    def get(self):
        user_forms = UserForm.query.all()
        serializer = UserFormSerializer(user_forms, many=True)
        return jsonify(serializer.data)


class UserFormDetailView:
    def get(self, user_form_id):
        user_form = UserForm.query.get_or_404(user_form_id)
        serializer = UserFormSerializer(user_form)
        return jsonify(serializer.data)
