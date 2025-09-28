"""
ASGI config for advanced_api_project project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
<<<<<<< HEAD
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
=======
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
>>>>>>> efee385d6c8f7a33a3a8e8e44a97537e13aecb57
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'advanced_api_project.settings')

application = get_asgi_application()
