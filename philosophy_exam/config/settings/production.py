from .base import *
from os import environ as os_environ

# хост
ALLOWED_HOSTS = ['127.0.0.1', 'bad-philosopher.ru', 'www.bad-philosopher.ru', "45.67.58.152"]

# # Database BEGET
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': '',
#         'USER': '',
#         'PASSWORD': '+',
#         'HOST': 'localhost',
#         'PORT': '3306',
#     }
# }

# Database DOCKER
DATABASES = {
    'default': {
        'ENGINE': os_environ.get('POSTGRES_ENGINE', 'django.db.backends.sqlite3'),
        'NAME': os_environ.get('POSTGRES_DB', str(ROOT_DIR.path('db.sqlite3')),),
        'USER': os_environ.get('POSTGRES_USER', 'user'),
        'PASSWORD': os_environ.get('POSTGRES_PASSWORD', 'password'),
        'HOST': os_environ.get('POSTGRES_HOST', 'localhost'),
        'PORT': os_environ.get('POSTGRES_PORT', '5432'),
    }
}