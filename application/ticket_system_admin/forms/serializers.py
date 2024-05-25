from marshmallow import Schema, fields


class TicketFormSerializer(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str(required=True)
    description = fields.Str(required=True)
    priority = fields.Str(required=True)
    status = fields.Str(required=True)


class CommentFormSerializer(Schema):
    id = fields.Int(dump_only=True)
    text = fields.Str(required=True)
    ticket = fields.Nested('TicketFormSerializer', only=['id', 'title'])


class UserFormSerializer(Schema):
    id = fields.Int(dump_only=True)
    username = fields.Str(required=True)
    email = fields.Email(required=True)
