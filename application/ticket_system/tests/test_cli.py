from app import db

from application.ticket_system.tests.test_models import test_user, test_ticket, test_group
from application.ticket_system.tests.test_routes import test_index, test_login, test_tickets, test_groups, \
    test_edit_group, test_delete_group


def test_auth():
    pass


def test_cli():
    db.create_all()
    test_user()
    test_group()
    test_ticket()
    test_index()
    test_login()
    test_tickets()
    test_groups()
    test_edit_group()
    test_delete_group()
    test_auth()
    db.drop_all()