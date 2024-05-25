from flask import Blueprint, render_template
from flask_login import login_required

from application.ticket_system_admin.models.group import Group

groups_bp = Blueprint('groups', __name__)


@groups_bp.route('/groups', methods=['GET'])
@login_required
def groups():
    groups = Group.query.all()
    return render_template('groups.html', groups=groups)


@groups_bp.route('/groups/<int:group_id>', methods=['GET'])
@login_required
def group(group_id):
    group = Group.query.get(group_id)
    return render_template('group.html', group=group)
