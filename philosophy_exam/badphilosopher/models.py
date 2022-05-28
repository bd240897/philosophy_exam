from django.db import models
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField

# модель ответов Антонюка
class Lections(models.Model):
    number = models.IntegerField()
    name_question = RichTextUploadingField(blank=True, null=True)
    answer = RichTextUploadingField(blank=True, null=True)
    visible = models.BooleanField(blank=True, null=True)
    url = models.SlugField(blank=True, null=True)

    def __str__(self):
        # для отображения в админке
        return str(self.number)