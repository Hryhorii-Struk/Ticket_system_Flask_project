from marshmallow import Schema, fields


class TicketSerializer(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str(required=True)
    description = fields.Str(required=True)
    priority = fields.Str(required=True)
    status = fields.Str(required=True)
    assigned_to = fields.Nested('UserSerializer', only=['id', 'username'])


class CommentSerializer(Schema):
    id = fields.Int(dump_only=True)
    text = fields.Str(required=True)
    ticket = fields.Nested('TicketSerializer', only=['id', 'title'])
    user = fields.Nested('UserSerializer', only=['id', 'username'])


class UserSerializer(Schema):
    id = fields.Int(dump_only=True)
    username = fields.Str(required=True)
    email = fields.Email(required=True)
