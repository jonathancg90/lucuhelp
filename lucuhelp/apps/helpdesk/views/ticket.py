# -*- coding: utf-8 -*-

from django.views.generic import TemplateView


class TicketTemplateView(TemplateView):
    template_name = 'tickets.html'
    
    def get_context_data(self, **kwargs):
        context = super(TicketTemplateView, self).get_context_data(**kwargs)
        context['menu'] = 'ticket'
        return context
