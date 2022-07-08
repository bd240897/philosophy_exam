# образ на основе которого создаём контейнер
FROM python:3.8.6-alpine

# рабочая директория внутри проекта
# ВНИМЕНИЕ - МЫ копирвем ТУТ только ТЕ файлы рядом с которыми тусит DockerFile!!!!!!!!!!!!!!!
# т.е. в папке будет (пример) /usr/src/mysite/manage.py
WORKDIR /usr/src/philosophy_exam

# переменные окружения для python
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Устанавливаем зависимости для Postgre
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

# устанавливаем зависимости
RUN pip install --upgrade pip
COPY ./requirements/production.txt .
COPY ./requirements/base.txt .
RUN pip install -r production.txt

# копируем содержимое текущей папки в контейнер
COPY . .

RUN chmod +x ./entrypoint.sh
COPY ./entrypoint.sh ./usr/src/philosophy_exam
ENTRYPOINT ["/usr/src/philosophy_exam/entrypoint.sh"]

RUN python -c "import django; django.setup(); \
   from django.contrib.auth.management.commands.createsuperuser import get_user_model; \
   get_user_model()._default_manager.db_manager('$DJANGO_DB_NAME').create_superuser( \
   username='$DJANGO_SUPERUSER_USERNAME', \
   email='$DJANGO_SUPERUSER_EMAIL', \
   password='$DJANGO_SUPERUSER_PASSWORD')

#ENTRYPOINT ["/usr/src/mysite/entrypoint.sh"]