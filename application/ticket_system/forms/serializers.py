from application.roles.serializers import Marshmallow
from application.ticket_system.forms.models import Ticket, Comment

ma = Marshmallow()


class TicketSerializer(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Ticket
        load_instance = True


class CommentSerializer(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Comment
        load_instance = True
