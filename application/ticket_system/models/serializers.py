from application.roles.serializers import Marshmallow
from application.ticket_system.forms.models import Ticket, Comment
from application.ticket_system.models.models import User

ma = Marshmallow()


class TicketSerializer(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Ticket


class CommentSerializer(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Comment


class UserSerializer(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
