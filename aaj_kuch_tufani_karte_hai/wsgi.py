"""
WSGI config for aaj_kuch_tufani_karte_hai project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'aaj_kuch_tufani_karte_hai.settings')

application = get_wsgi_application()
