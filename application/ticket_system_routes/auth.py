from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_user, logout_user, login_required

from application.ticket_system.scripts.auth import User

auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and user.password == password:
            login_user(user)
            return redirect(url_for('main.index'))
    return render_template('login.html')


@auth_bp.route('/logout', methods=['POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))
