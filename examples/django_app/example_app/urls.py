from django.conf.urls import include
from django.urls import re_path
from django.contrib import admin
from example_app.views import ChatterBotAppView, ChatterBotApiView


urlpatterns = [
    re_path(r'^$', ChatterBotAppView.as_view(), name='main'),
    re_path(r'^admin/', admin.site.urls, name='admin'),
    re_path(r'^api/chatterbot/', ChatterBotApiView.as_view(), name='chatterbot'),
]
