from flask import jsonify

from .models import Role, Group
from .serializers import RoleSerializer, GroupSerializer


def get():
    roles = Role.query.all()
    serializer = RoleSerializer(roles, many=True)
    return jsonify(serializer.data)


class RoleListView:

    @classmethod
    def as_view(cls, param):
        pass


class RoleDetailView:
    def get(self, role_id):
        role = Role.query.get_or_404(role_id)
        serializer = RoleSerializer(role)
        return jsonify(serializer.data)

    @classmethod
    def as_view(cls, param):
        pass


def get():
    groups = Group.query.all()
    serializer = GroupSerializer(groups, many=True)
    return jsonify(serializer.data)


class GroupListView:

    @classmethod
    def as_view(cls, param):
        pass


def get(group_id):
    group = Group.query.get_or_404(group_id)
    serializer = GroupSerializer(group)
    return jsonify(serializer.data)


class GroupDetailView:

    @classmethod
    def as_view(cls, param):
        pass
