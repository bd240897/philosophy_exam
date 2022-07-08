#!/bin/sh

python manage.py migrate
python manage.py makemigrations badphilosopher
python manage.py makemigrations contact
python manage.py migrate
python manage.py loaddata db.json

python manage.py shell -c "from django.contrib.auth.models import User; User.objects.create_superuser('$DJANGO_SUPERUSER_USERNAME', '$DJANGO_SUPERUSER_EMAIL', '$DJANGO_SUPERUSER_PASSWORD')"

exec "$@"