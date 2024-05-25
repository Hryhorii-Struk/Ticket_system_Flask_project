from application.roles.models import Role, Group


class Marshmallow:
    def __init__(self):
        self.SQLAlchemyAutoSchema = None

    pass


ma = Marshmallow()


class RoleSerializer(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Role
        load_instance = True


class GroupSerializer(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Group
        load_instance = True
