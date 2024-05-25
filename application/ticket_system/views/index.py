

from flask import render_template
from flask_login import login_required

from . import flicket_bp
from application import app
from application.ticket_system.scripts.pie_charts import create_pie_chart_dict
from application.ticket_system.models.ticket_system_models import FlicketTicket


# view users
@flicket_bp.route(app.config['FLICKET'], methods=['GET', 'POST'])
@login_required
def index():
    """ View showing ticket_system main page. We use this to display some statistics."""
    days = 7

    # CAROUSEL
    tickets = FlicketTicket.carousel_query()

    # PIE CHARTS
    ids, graph_json = create_pie_chart_dict()

    return render_template('ticket_system_index.html',
                           days=days,
                           tickets=tickets,
                           ids=ids,
                           graph_json=graph_json)
