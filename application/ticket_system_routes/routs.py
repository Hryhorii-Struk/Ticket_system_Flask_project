from flask import render_template, redirect, url_for, flash
from app import app, db, Ticket
from flask_login import login_required

from application.ticket_system.forms.ticket_system_forms import TicketForm


@app.route('/ticket', methods=['GET', 'POST'])
@login_required
def ticket_index():
    form = TicketForm()
    if form.validate_on_submit():
        ticket = Ticket(title=form.title.data, description=form.description.data, status=form.status.data,
                        user_id=form.user_id.data, group_id=form.group_id.data, note=form.note.data)
        db.session.add(ticket)
        db.session.commit()
        flash('Ticket created successfully')
        return redirect(url_for('ticket_index'))
    tickets = Ticket.query.all()
    return render_template('ticket/index.html', form=form, tickets=tickets)


@app.route('/ticket/<int:ticket_id>', methods=['GET', 'POST'])
@login_required
def ticket_detail(ticket_id):
    ticket = Ticket.query.get_or_404(ticket_id)
    form = TicketForm(obj=ticket)
    if form.validate_on_submit():
        ticket.title = form.title.data
        ticket.description = form.description.data
        ticket.status = form.status.data
        ticket.user_id = form.user_id.data
        ticket.group_id = form.group_id.data
        ticket.note = form.note.data
        db.session.commit()
        flash('Ticket updated successfully')
        return redirect(url_for('ticket_detail', ticket_id=ticket_id))
    return render_template('ticket/detail.html', form=form, ticket=ticket)
