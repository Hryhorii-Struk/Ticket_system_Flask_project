from application.ticket_system.tests.test_models import test_user, test_group, test_ticket


def test_database():
    test_user()
    test_group()
    test_ticket()
