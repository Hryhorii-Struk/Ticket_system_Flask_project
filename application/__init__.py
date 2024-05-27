

"""

    Flicket
    =======

    A simple ticket system using Python and the Flask microframework.

    This probably wouldn't have been created without the excellent tutorials written by Miguel Grinberg:
    https://blog.miguelgrinberg.com. Many thanks kind sir.


"""

from flask import abort
from flask import Flask
from flask import g
from flask import request
from flask_login import LoginManager
from flask_mail import Mail
from flask_pagedown import PageDown
from flask_sqlalchemy import SQLAlchemy
from flask_babel import Babel
from flaskext.markdown import Markdown
from flask_migrate import Migrate

from application.ticket_system_admin.views import admin_bp
from application.ticket_system_api.views import bp_api
from application.ticket_system_errors import bp_errors
from application.ticket_system.views import flicket_bp
from application.ticket_system.scripts.jinja2_functions import now_year

__version__ = '0.3.4'

app = Flask(__name__)
app.config.from_object('config.BaseConfiguration')
app.config.update(TEMPLATES_AUTO_RELOAD=True)

db = SQLAlchemy(app)
migrate = Migrate(app, db)
mail = Mail(app)
pagedown = PageDown(app)


Markdown(app)

# import jinja function
app.jinja_env.globals.update(now_year=now_year)

# import models so alembic can see them
# noinspection PyPep8
from application.ticket_system.models import ticket_system_user, ticket_system_models
# noinspection PyPep8
from application.ticket_system_admin.models import ticket_system_config

lm = LoginManager()
lm.init_app(app)
lm.login_view = 'flicket_bp.login'

# noinspection PyPep8
from .ticket_system_admin.views import view_admin
# noinspection PyPep8
from .ticket_system_admin.views import view_config
# noinspection PyPep8
from .ticket_system_admin.views import view_email_test

# noinspection PyPep8
from .ticket_system.views import assign
# noinspection PyPep8
from .ticket_system.views import categories
# noinspection PyPep8
from .ticket_system.views import edit_status
# noinspection PyPep8
from .ticket_system.views import claim
# noinspection PyPep8
from .ticket_system.views import create
# noinspection PyPep8
from .ticket_system.views import delete
# noinspection PyPep8
from .ticket_system.views import departments
# noinspection PyPep8
from .ticket_system.views import edit
# noinspection PyPep8
from .ticket_system.views import history
# noinspection PyPep8
from .ticket_system.views import index
# noinspection PyPep8
from .ticket_system.views import login
# noinspection PyPep8
from .ticket_system.views import help
# noinspection PyPep8
from .ticket_system.views import tickets
# noinspection PyPep8
from .ticket_system.views import release
# noinspection PyPep8
from .ticket_system.views import render_uploads
# noinspection PyPep8
from .ticket_system.views import subscribe
# noinspection PyPep8
from .ticket_system.views import user_edit
# noinspection PyPep8
from .ticket_system.views import users
# noinspection PyPep8
from .ticket_system.views import view_ticket
# noinspection PyPep8
from .ticket_system.views import department_category

# noinspection PyPep8
from .ticket_system_api.views import actions
# noinspection PyPep8
from .ticket_system_api.views import categories
# noinspection PyPep8
from .ticket_system_api.views import departments
# noinspection PyPep8
from .ticket_system_api.views import histories
# noinspection PyPep8
from .ticket_system_api.views import posts
# noinspection PyPep8
from .ticket_system_api.views import priorities
# noinspection PyPep8
from .ticket_system_api.views import status
# noinspection PyPep8
from .ticket_system_api.views import subscriptions
# noinspection PyPep8
from .ticket_system_api.views import tickets
# noinspection PyPep8
from .ticket_system_api.views import tokens
# noinspection PyPep8
from .ticket_system_api.views import uploads
# noinspection PyPep8
from .ticket_system_api.views import users
from .ticket_system_api.views import department_categories

# noinspection PyPep8
from .ticket_system_errors import handlers

app.register_blueprint(admin_bp)
app.register_blueprint(flicket_bp)
app.register_blueprint(bp_api)
app.register_blueprint(bp_errors)


# prints url routes for debugging
# for rule in app.url_map.iter_rules():
#    print(rule)


def get_locale():
    # if a user is logged in, use the locale from the user settings
    user = getattr(g, 'user', None)
    if hasattr(user, 'locale'):
        return user.locale
    # otherwise try to guess the language from the user accept
    # header the browser transmits.  We support de/fr/en in this
    # example.  The best match wins.
    return request.accept_languages.best_match(app.config['SUPPORTED_LANGUAGES'].keys())


babel = Babel(app)
babel.init_app(app, locale_selector=get_locale)

@app.url_defaults
def set_language_code(endpoint, values):
    if 'lang_code' in values or not g.get('lang_code', None):
        return
    if app.url_map.is_endpoint_expecting(endpoint, 'lang_code'):
        values['lang_code'] = g.lang_code


@app.url_value_preprocessor
def get_lang_code(endpoint, values):
    if values is not None:
        g.lang_code = values.pop('lang_code', None)


@app.before_request
def ensure_lang_support():
    lang_code = g.get('lang_code', None)
    if lang_code and lang_code not in app.config['SUPPORTED_LANGUAGES'].keys():
        return abort(404)


from application.commands import register_clicks

register_clicks(app)


