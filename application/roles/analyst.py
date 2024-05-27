from application.roles.models import Role
from application.ticket_system.forms.models import Ticket


class Analyst(Role):
    def __init__(self):
        super().__init__()
        self.assigned_group = None
        self.name = "Analyst"
        self.description = "Analyst role"

    def assign_group(self, group):
        self.assigned_group = group

    def get_tickets(self):
        # Assuming there's a Ticket class with a group attribute
        return [ticket for ticket in Ticket.all() if ticket.group == self.assigned_group]
