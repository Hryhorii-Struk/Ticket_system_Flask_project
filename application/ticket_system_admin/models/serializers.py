from flask import Flask

app = Flask(__name__)


class Ticket:
    def __init__(self, id, title, description, status, created_at, updated_at):
        self.id = id
        self.title = title
        self.description = description
        self.status = status
        self.created_at = created_at
        self.updated_at = updated_at


class TicketSerializerManual:
    def __init__(self, data=None):
        self.data = data

    def is_valid(self):
        if not self.data or not self.data.get('title') or not self.data.get('description'):
            return False
        return True

    def save(self):
        if not self.is_valid():
            return None
        ticket = Ticket(
            id=None,
            title=self.data.get('title'),
            description=self.data.get('description'),
            status='open',
            created_at=None,
            updated_at=None
        )

        return ticket


if __name__ == '__main__':
    serializer = TicketSerializerManual(data={'title': 'New Ticket', 'description': 'This is a new ticket'})
    if serializer.is_valid():
        ticket = serializer.save()
        print(ticket)


class TicketSerializer:
    def __init__(self):
        self.data = None

    def is_valid(self):
        pass

    def save(self):
        pass