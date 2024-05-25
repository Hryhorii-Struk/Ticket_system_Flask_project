from flask import Flask
from roles import roles_blueprint

app = Flask(__name__)

app.register_blueprint(roles_blueprint, url_prefix="/roles")