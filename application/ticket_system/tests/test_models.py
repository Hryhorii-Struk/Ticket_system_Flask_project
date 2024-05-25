from app import db, User, Group, Ticket


def test_user():
    user = User(username='testuser', password='testpassword', role='admin')
    db.session.add(user)
    db.session.commit()
    assert User.query.count() == 1

def test_group():
    group = Group(name='testgroup')
    db.session.add(group)
    db.session.commit()
    assert Group.query.count() == 1

def test_ticket():
    group = Group(name='testgroup')
    db.session.add(group)
    db.session.commit()
    ticket = Ticket(title='testticket', description='testdescription', group=group)
    db.session.add(ticket)
    db.session.commit()
    assert Ticket.query.count() == 1