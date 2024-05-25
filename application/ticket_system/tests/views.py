import unittest

from application.ticket_system.forms.views import TicketListView, TicketDetailView, CommentListView, CommentDetailView
from application.ticket_system.models.views import UserListView, UserDetailView


class TestViews(unittest.TestCase):
    def test_ticket_list_view(self):
        view = TicketListView()
        self.assertIsNotNone(view)

    def test_ticket_detail_view(self):
        view = TicketDetailView()
        self.assertIsNotNone(view)

    def test_comment_list_view(self):
        view = CommentListView()
        self.assertIsNotNone(view)

    def test_comment_detail_view(self):
        view = CommentDetailView()
        self.assertIsNotNone(view)

    def test_user_list_view(self):
        view = UserListView()
        self.assertIsNotNone(view)

    def test_user_detail_view(self):
        view = UserDetailView()
        self.assertIsNotNone(view)


if __name__ == '__main__':
    unittest.main()
