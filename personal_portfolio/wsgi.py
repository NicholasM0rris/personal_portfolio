"""
WSGI config for personal_portfolio project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'personal_portfolio.settings')
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'stats.settings')
application = get_wsgi_application()
application = DjangoWhiteNoise(application)
