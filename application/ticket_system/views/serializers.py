import types

from marshmallow import Schema, fields
from sqlalchemy import null


class TicketSerializer(Schema):
    def __init__(
            self,
            *,
            only: types.StrSequenceOrSet | None = None,
            exclude: types.StrSequenceOrSet = (),
            many: bool = False,
            context: dict | None = None,
            load_only: types.StrSequenceOrSet = (),
            dump_only: types.StrSequenceOrSet = (),
            partial: bool | types.StrSequenceOrSet | None = None,
            unknown: str | None = None,
    ):
        super().__init__(null, only, exclude, many, context, load_only, dump_only, partial, unknown)
        self.data = None

    id = fields.Int(dump_only=True)
    title = fields.Str(required=True)
    description = fields.Str(required=True)
    priority = fields.Str(required=True)
    status = fields.Str(required=True)
    assigned_to = fields.Nested('UserSerializer', only=['id', 'username'])


class CommentSerializer(Schema):
    def __init__(
            self,
            *,
            only: types.StrSequenceOrSet | None = None,
            exclude: types.StrSequenceOrSet = (),
            many: bool = False,
            context: dict | None = None,
            load_only: types.StrSequenceOrSet = (),
            dump_only: types.StrSequenceOrSet = (),
            partial: bool | types.StrSequenceOrSet | None = None,
            unknown: str | None = None,
    ):
        super().__init__(null, only, exclude, many, context, load_only, dump_only, partial, unknown)
        self.data = None

    id = fields.Int(dump_only=True)
    text = fields.Str(required=True)
    ticket = fields.Nested('TicketSerializer', only=['id', 'title'])
    user = fields.Nested('UserSerializer', only=['id', 'username'])


class UserSerializer(Schema):
    def __init__(
            self,
            *,
            only: types.StrSequenceOrSet | None = None,
            exclude: types.StrSequenceOrSet = (),
            many: bool = False,
            context: dict | None = None,
            load_only: types.StrSequenceOrSet = (),
            dump_only: types.StrSequenceOrSet = (),
            partial: bool | types.StrSequenceOrSet | None = None,
            unknown: str | None = None,
    ):
        super().__init__(null, only, exclude, many, context, load_only, dump_only, partial, unknown)
        self.data = None

    id = fields.Int(dump_only=True)
    username = fields.Str(required=True)
    email = fields.Email(required=True)
