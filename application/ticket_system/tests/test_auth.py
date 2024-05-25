from app import db, User


def test_login(client):
    user = User(username='testuser', password='testpassword', role='admin')
    db.session.add(user)
    db.session.commit()
    response = client.post('/login', data={'username': 'testuser', 'password': 'testpassword'})
    assert response.status_code == 302
    assert response.headers['Location'] == 'http://localhost/tickets'


def test_logout(client):
    user = User(username='testuser', password='testpassword', role='admin')
    db.session.add(user)
    db.session.commit()
    client.post('/login', data={'username': 'testuser', 'password': 'testpassword'})
    response = client.get('/logout')
    assert response.status_code == 302
    assert response.headers['Location'] == 'http://localhost/'


def test_unauthorized(client):
    user = User(username='testuser', password='testpassword', role='admin')
    db.session.add(user)
    db.session.commit()
    response = client.get('/groups', headers={'Authorization': 'Basic ' + user.encode_auth()})
    assert response.status_code == 401
