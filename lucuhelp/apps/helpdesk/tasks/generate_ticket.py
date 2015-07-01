from celery.task import PeriodicTask
from datetime import timedelta
from apps.helpdesk.models.Ticket import Ticket
from apps.helpdesk.models.Client import Client


class GenerateTicket(PeriodicTask):
    run_every = timedelta(minutes=1)

    def run(self, **kwargs):
        ticket = Ticket()
        ticket.client = Client.objects.all().first()
        ticket.description = 'description'
        ticket.subject = 'subject'
        ticket.save()
