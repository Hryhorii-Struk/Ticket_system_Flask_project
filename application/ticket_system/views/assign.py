

import datetime

from flask import redirect, url_for, flash, render_template
from flask_babel import gettext
from flask_login import login_required

from application import app, db
from application.ticket_system.forms.ticket_system_forms import AssignUserForm
from application.ticket_system.models.ticket_system_models import FlicketTicket, FlicketStatus, FlicketSubscription
from application.ticket_system.models.ticket_system_user import FlicketUser
from application.ticket_system.scripts.ticket_system_functions import add_action
from application.ticket_system.scripts.email import FlicketMail
from . import flicket_bp


# tickets main
@flicket_bp.route(app.config['FLICKET'] + 'ticket_assign/<int:ticket_id>/', methods=['GET', 'POST'])
@login_required
def ticket_assign(ticket_id=False):
    form = AssignUserForm()
    ticket = FlicketTicket.query.filter_by(id=ticket_id).one()

    if ticket.current_status.status == 'Closed':
        flash(gettext("Can't assign a closed ticket."), category='warning')
        return redirect(url_for('flicket_bp.ticket_view', ticket_id=ticket_id))

    if form.validate_on_submit():

        user = FlicketUser.query.filter_by(username=form.username.data).first()

        if ticket.assigned == user:
            flash(gettext('User is already assigned to ticket.'), category='warning')
            return redirect(url_for('flicket_bp.ticket_view', ticket_id=ticket.id))

        # set status to in work
        status = FlicketStatus.query.filter_by(status='In Work').first()
        # assign ticket
        ticket.assigned = user
        ticket.current_status = status
        ticket.last_updated = datetime.datetime.now()

        if not user.total_assigned:
            user.total_assigned = 1
        else:
            user.total_assigned += 1

        # add action record
        add_action(ticket, 'assign', recipient=user)

        # subscribe to the ticket
        if not ticket.is_subscribed(user):
            subscribe = FlicketSubscription(
                ticket=ticket,
                user=user
            )
            db.session.add(subscribe)

        db.session.commit()

        # send email to state ticket has been assigned.
        f_mail = FlicketMail()
        f_mail.assign_ticket(ticket)

        flash(gettext('You reassigned ticket: {} to {}'.format(ticket.id, user.name)), category='success')
        return redirect(url_for('flicket_bp.ticket_view', ticket_id=ticket.id))

    title = gettext('Assign Ticket')

    return render_template("ticket_system_assign.html", title=title, form=form, ticket=ticket)
