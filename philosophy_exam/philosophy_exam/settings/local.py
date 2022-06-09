from .base import *

# секретный ключ - ТУТ НЕ НУЖЕН
SECRET_KEY = env('DJANGO_SECRET_KEY', default='django-insecure-7r3vs91=fa)v8yh4g7h=l#0e))om%8n!n4i*^iv%=o=88w%-dr')

# дебаг
DEBUG = env.bool('DJANGO_DEBUG', default=True)
