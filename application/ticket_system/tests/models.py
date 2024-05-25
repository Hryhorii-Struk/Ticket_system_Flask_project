import unittest

from application.ticket_system.forms.models import Ticket, Comment
from application.ticket_system.models.models import User


class TestModels(unittest.TestCase):
    def test_ticket_model(self):
        ticket = Ticket(title='Test ticket', description='Test description', priority='high')
        self.assertIsNotNone(ticket)

    def test_comment_model(self):
        comment = Comment(text='Test comment')
        self.assertIsNotNone(comment)

    def test_user_model(self):
        user = User(username='test_user', email='test@example.com')
        self.assertIsNotNone(user)


if __name__ == '__main__':
    unittest.main()
