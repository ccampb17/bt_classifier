import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent

PROJECT_NAME = 'old_red_lion'

SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', 'f4cuk(!pf)_@o1fkqk$5(h85nzq@%voh_hc02*_35eo_rppf=x')

APPENV = os.getenv('DJANGO_APP_ENV', "LOCAL")

DEBUG = int(os.getenv("DJANGO_DEBUG", default=0))

ROOT_URLCONF = f'{PROJECT_NAME}.urls'

WSGI_APPLICATION = f'{PROJECT_NAME}.wsgi.application'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
