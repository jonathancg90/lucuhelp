from django.conf.urls import patterns, url

from apps.helpdesk.views.dashboard import DashboardTemplateView
from apps.helpdesk.views.ticket import TicketTemplateView
from apps.helpdesk.views.config import ConfigView


urlpatterns = patterns('',
                       url(r'^$',
                           DashboardTemplateView.as_view(),
                           name='dashboard_view'),
                       url(r'ticket/$',
                           TicketTemplateView.as_view(),
                           name='ticket_view'),
                       url(r'config/(?P<pk>\d+)/$',
                           ConfigView.as_view(),
                           name='config_view'),

                       )