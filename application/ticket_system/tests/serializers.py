import unittest

from application.ticket_system.forms.models import Ticket, Comment
from application.ticket_system.forms.serializers import TicketSerializer, CommentSerializer
from application.ticket_system.models.models import User
from application.ticket_system.models.serializers import UserSerializer


class TestSerializers(unittest.TestCase):
    def test_ticket_serializer(self):
        ticket = Ticket(title='Test ticket', description='Test description', priority='high')
        serializer = TicketSerializer(ticket)
        self.assertIsNotNone(serializer.data)

    def test_comment_serializer(self):
        comment = Comment(text='Test comment')
        serializer = CommentSerializer(comment)
        self.assertIsNotNone(serializer.data)

    def test_user_serializer(self):
        user = User(username='test_user', email='test@example.com')
        serializer = UserSerializer(user)
        self.assertIsNotNone(serializer.data)


if __name__ == '__main__':
    unittest.main()
