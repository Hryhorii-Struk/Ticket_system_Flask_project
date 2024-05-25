from urllib import request

from app import app

from flask import redirect, render_template, url_for
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required

login_manager = LoginManager(app)


class User(UserMixin):
    query = None

    def __init__(self, user_id):
        self.id = user_id

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id

    def encode_auth(self):
        pass


@login_manager.user_loader
def load_user(user_id):
    user = User.query.get(user_id)
    if user:
        return User(user_id)
    return None


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and user.password == password:
            login_user(User(user.id))
            return redirect(url_for('main.index'))
    return render_template('login.html')


@app.route('/logout', methods=['POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))
