from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import  current_user
from functools import wraps

from application import db
from application.ticket_system_admin.models.group import Group

group_bp = Blueprint('group', __name__)


def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if current_user.role != 'admin':
            return redirect(url_for('main.index'))
        return f(*args, **kwargs)
    return decorated_function


@group_bp.route('/groups', methods=['GET'])
@admin_required
def groups():
    groups = Group.query.all()
    return render_template('groups.html', groups=groups)


@group_bp.route('/groups/<int:group_id>/edit', methods=['GET', 'POST'])
@admin_required
def edit_group(group_id):
    group = Group.query.get(group_id)
    if request.method == 'POST':
        group.name = request.form['name']
        db.session.commit()
        return redirect(url_for('group.groups'))
    return render_template('edit_group.html', group=group)


@group_bp.route('/groups/<int:group_id>/delete', methods=['POST'])
@admin_required
def delete_group(group_id):
    group = Group.query.get(group_id)
    if group:
        db.session.delete(group)
        db.session.commit()
    return redirect(url_for('group.groups'))
