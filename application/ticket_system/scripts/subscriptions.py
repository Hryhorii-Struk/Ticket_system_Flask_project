


from application import db
from application.ticket_system.models.ticket_system_models import FlicketSubscription
from application.ticket_system.scripts.ticket_system_functions import add_action


def subscribe_user(ticket, user):
    if not ticket.is_subscribed(user):
        # subscribe user to ticket
        # noinspection PyArgumentList
        subscribe = FlicketSubscription(user=user, ticket=ticket)
        add_action(ticket, 'subscribe', recipient=user)
        db.session.add(subscribe)
        db.session.commit()
        return True

    return False
