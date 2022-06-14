from django.db import models
from django.utils import timezone


class Comment(models.Model):
    TITLE_CHOICES = (
        ("1", "Сообщение об ошибках"),
        ("2", "Советы и рекомендации"),
        ("3", "Хочу связаться с автором"))

    name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    message = models.TextField(max_length=500)
    purpose = models.CharField(max_length=3, choices=TITLE_CHOICES, default='1')
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name