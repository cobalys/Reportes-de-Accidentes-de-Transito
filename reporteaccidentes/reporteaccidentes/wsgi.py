import os

os.environ['DJANGO_SETTINGS_MODULE'] = "reporteaccidentes.settings"
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
