# -*- coding: utf-8 -*-

from django.views.generic import UpdateView
from apps.helpdesk.models.Config import Config
from apps.helpdesk.forms.config import ConfigForm


class ConfigView(UpdateView):
    template_name = 'config.html'
    model = Config
    form_class = ConfigForm

    def get_context_data(self, **kwargs):
        context = super(ConfigView, self).get_context_data(**kwargs)
        context['menu'] = 'config'
        return context
