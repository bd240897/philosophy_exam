from django.db import models
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField

# модель ответов Антонюка
class Lections(models.Model):
    number = models.IntegerField(unique=True)
    name_question = models.TextField(blank=True, null=True)
    answer = RichTextUploadingField(blank=True, null=True)
    visible = models.BooleanField(blank=True, null=True)

    def __str__(self):
        # для отображения в админке
        return str(self.number)

# модель ответов Фурсова
class Seminars(models.Model):
    number = models.IntegerField(unique=True)
    name_question = models.TextField(blank=True, null=True)
    answer = RichTextUploadingField(blank=True, null=True)
    visible = models.BooleanField(blank=True, null=True)

    def __str__(self):
        # для отображения в админке
        return str(self.number)