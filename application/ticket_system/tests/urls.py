import unittest

from application import app


class TestUrls(unittest.TestCase):
    def test_ticket_list_url(self):
        tester = app
        response = tester.get('/tickets/')
        self.assertEqual(response.status_code, 200)

    def test_ticket_detail_url(self):
        tester = app
        response = tester.get('/tickets/1/')
        self.assertEqual(response.status_code, 200)

    def test_comment_list_url(self):
        tester = app
        response = tester.get('/comments/')
        self.assertEqual(response.status_code, 200)

    def test_comment_detail_url(self):
        tester = app
        response = tester.get('/comments/1/')
        self.assertEqual(response.status_code, 200)

    def test_user_list_url(self):
        tester = app
        response = tester.get('/urls.py/')
        self.assertEqual(response.status_code, 200)

    def test_user_detail_url(self):
        tester = app
        response = tester.get('/urls.py/1/')
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
