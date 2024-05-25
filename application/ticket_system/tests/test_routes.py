from app import Group

from application import db
from application.ticket_system.scripts.auth import User


def test_index(client):
    response = client.get('/')
    assert response.status_code == 200


def test_login(client):
    response = client.get('/login')
    assert response.status_code == 200


def test_tickets(client):
    user = User(username='testuser', password='testpassword', role='admin')
    db.session.add(user)
    db.session.commit()
    response = client.get('/tickets', headers={'Authorization': 'Basic ' + user.encode_auth()})
    assert response.status_code == 200


def test_groups(client):
    user = User(username='testuser', password='testpassword', role='admin')
    db.session.add(user)
    db.session.commit()
    response = client.get('/groups', headers={'Authorization': 'Basic ' + user.encode_auth()})
    assert response.status_code == 200


def test_edit_group(client):
    user = User(username='testuser', password='testpassword', role='admin')
    db.session.add(user)
    db.session.commit()
    group = Group(name='testgroup')
    db.session.add(group)
    db.session.commit()
    response = client.get('/groups/1/edit', headers={'Authorization': 'Basic ' + user.encode_auth()})
    assert response.status_code == 200


def test_delete_group(client):
    user = User(username='testuser', password='testpassword', role='admin')
    db.session.add(user)
    db.session.commit()
    group = Group(name='testgroup')
    db.session.add(group)
    db.session.commit()
    response = client.post('/groups/1/delete', headers={'Authorization': 'Basic ' + user.encode_auth()})
    assert response.status_code == 302
