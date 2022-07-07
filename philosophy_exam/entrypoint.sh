#!/bin/sh

python manage.py migrate
python manage.py makemigrations badphilosopher
python manage.py makemigrations contact
python manage.py migrate

if [ "$DJANGO_SUPERUSER_USERNAME" ]
then
    python manage.py createsuperuser \
        --username $DJANGO_SUPERUSER_USERNAME \
        --email DJANGO_SUPERUSER_EMAIL
fi

exec "$@"