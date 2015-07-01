
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    url(r'^', include('apps.public.urls')),

    url(r'^panel/', include('apps.helpdesk.urls')),

    url(
        r'^social/',
        include('social.apps.django_app.urls', namespace='social')
    ),
]
