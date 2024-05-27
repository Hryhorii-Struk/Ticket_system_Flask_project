from flask import render_template, redirect, url_for, flash

from application import db
from flask_login import login_required, current_user

from application.ticket_system.forms.models import Ticket
from application.ticket_system.forms.ticket_system_forms import TicketForm


@login_required
def index():
    tickets = Ticket.query.filter_by(assigned_to=current_user.id).all()
    return render_template('analysts/index.html', tickets=tickets)


@login_required
def create():
    form = TicketForm()
    if form.validate_on_submit():
        ticket = Ticket(
            status='Pending',
            assigned_to=current_user.id,
            created_by=current_user.id,
            title=form.title.data,
            description=form.description.data
        )
        db.session.add(ticket)
        db.session.commit()
        flash('Ticket created successfully.', 'success')
        return redirect(url_for('analysts.index'))
    return render_template('analysts/create.html', form=form)


@login_required
def update(id):
    ticket = Ticket.query.get_or_404(id)
    form = TicketForm()
    if form.validate_on_submit():
        ticket.title = form.title.data
        ticket.description = form.description.data
        db.session.commit()
        flash('Ticket updated successfully.', 'success')
        return redirect(url_for('analysts.index'))
    form.title.data = ticket.title
    form.description.data = ticket.description
    return render_template('analysts/update.html', form=form, ticket=ticket)


@login_required
def delete(id):
    ticket = Ticket.query.get_or_404(id)
    db.session.delete(ticket)
    db.session.commit()
    flash('Ticket deleted successfully.', 'success')
    return redirect(url_for('analysts.index'))
