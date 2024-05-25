

from flask import Blueprint

import os

static_folder = os.path.join(os.getcwd(), 'application/ticket_system/static')

flicket_bp = Blueprint('flicket_bp', __name__,
                       template_folder="../templates",
                       static_folder=static_folder,
                       static_url_path='/ticket_system/static',
                       )
