from django.conf.urls import patterns, include, url

from apps.public.views.home import HomeTemplateView

urlpatterns = patterns('',
                       url(r'^$',
                           HomeTemplateView.as_view(),
                           name='home_view'),

                       )