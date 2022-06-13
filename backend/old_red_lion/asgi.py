import os

from django.core.asgi import get_asgi_application

from old_red_lion.settings import PROJECT_NAME

os.environ.setdefault('DJANGO_SETTINGS_MODULE', f'{PROJECT_NAME}.settings')

application = get_asgi_application()
