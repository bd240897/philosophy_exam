from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Comment


class BlogTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@email.com',
            password='secret'
        )

        self.post = Comment.objects.create(
            name='Dima',
            email='1@mail.ru',
            message='Hi everyone',
            purpose=1,
        )

    def test_comment_count(self):
        post = Comment.objects.all().count()
        self.assertEqual(post, 1)

    def test_comment_content(self):
        post = Comment.objects.get(name="Dima")
        self.assertEqual(f'{post.name}', 'Dima')
        self.assertEqual(f'{post.email}', '1@mail.ru')
        self.assertEqual(f'{post.message}', 'Hi everyone')

    def test_comment_template(self):
        response = self.client.get(reverse('comment_form'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact/comment_form.html')

# took from
# Формы для блога на Django: CreateView, UpdateView и DeleteView
# https://python-scripts.com/django-forms

# Руководство часть 10: Тестирование приложений Django
# https://developer.mozilla.org/ru/docs/Learn/Server-side/Django/Testing
# Django Tutorial Part 9: Working with forms
# https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Forms

# Немного подробностей про Class Based Views, ч.4
# https://habr.com/ru/post/137960/

# Классы представлений: ListView, DetailView, CreateView
# https://proproprogs.ru/django/klassy-predstavleniy-listview-detailview-createview

# Где и как учить django?
# https://www.youtube.com/watch?v=JjugsugXop4

# Бекенд на Django, Урок 2: Unit Tests
# https://www.youtube.com/watch?v=FquXN0t_KbU&t=1824s