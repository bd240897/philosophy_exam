from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
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

    def get_absolute_url(self):
        return reverse("lections_detailed_answer", kwargs={"slug": self.number})


# модель ответов Фурсова
class Seminars(models.Model):
    number = models.IntegerField(unique=True)
    name_question = models.TextField(blank=True, null=True)
    answer = RichTextUploadingField(blank=True, null=True)
    visible = models.BooleanField(blank=True, null=True)

    def __str__(self):
        # для отображения в админке
        return str(self.number)

    def get_absolute_url(self):
        return reverse("seminars_detailed_answer", kwargs={"slug": self.number})


class CommentLection(models.Model):
    author = models.CharField(verbose_name="Автор", max_length=100)
    text = models.TextField(verbose_name="Текст", max_length=300)
    post = models.ForeignKey('Lections', verbose_name="Лекция", on_delete=models.CASCADE)
    parent = models.ForeignKey('self', verbose_name="Родитель", on_delete=models.SET_NULL, blank=True, null=True)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        # для отображения в админке
        return self.author

# from badphilosopher.models import Lections, Seminars, CommentLection
# f = Lections.objects.get(number=1)
# print(f.commentlection_set.all())