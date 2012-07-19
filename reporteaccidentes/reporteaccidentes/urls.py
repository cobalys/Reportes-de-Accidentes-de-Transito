from django.conf import settings
from django.conf.urls.defaults import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from reporteaccidentes.accidentes.views import index, get_top, about, top
import django

urlpatterns = patterns('',
     (r'^$', index),
     (r'^update.ajax', get_top),
     (r'^ranking.html', top),
     (r'^about.html', about),
)

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
