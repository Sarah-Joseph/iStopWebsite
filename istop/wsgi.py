"""
WSGI config for istop project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
import sys

sys.path.append('/opt/bitnami/apps/django/django_projects/istop')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "istop.settings")

application = get_wsgi_application()
