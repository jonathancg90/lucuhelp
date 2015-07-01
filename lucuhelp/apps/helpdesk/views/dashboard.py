# -*- coding: utf-8 -*-

from django.views.generic import TemplateView
from apps.helpdesk.models.Ticket import Ticket


class DashboardTemplateView(TemplateView):
    template_name = 'dashboard.html'
    
    def get_tickets(self):
        tickets_open = Ticket.objects.filter(status=Ticket.STATUS_OPEN).order_by('created')
        tickets_pending = Ticket.objects.filter(status=Ticket.STATUS_PENDING).order_by('created')
        tickets_reopened = Ticket.objects.filter(status=Ticket.STATUS_REOPENED).order_by('created')
        tickets_solved = Ticket.objects.filter(status=Ticket.STATUS_SOLVED).order_by('created')
        return {
            'tickets_open': tickets_open,
            'tickets_pending': tickets_pending,
            'tickets_reopened': tickets_reopened,
            'tickets_solved': tickets_solved
        }

    def get_context_data(self, **kwargs):
        context = super(DashboardTemplateView, self).get_context_data(**kwargs)
        context['tickets'] = self.get_tickets()
        return context