from django.shortcuts import render, get_object_or_404
from django.views import View
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import redirect
from django.views.generic import ListView, DetailView

from .models import Lections, Seminars

class LectionsAnswerListView(ListView):
    """ Список вопросов """
    model = Lections
    paginate_by = 10
    queryset = Lections.objects.order_by('number').all()
    context_object_name = 'achieves_obj'
    template_name = "badphilosopher/lections_answer_list.html"

class LectionsDetailedAnswerlView(DetailView):
    """ Страница одного ответа"""
    model = Lections
    slug_field = "number"
    context_object_name = "answer"
    template_name = 'badphilosopher/detailed_answer.html'

class MainPagelView(View):
    """Главная страница"""

    def get(self, request, *args, **kwargs):
        return render(request, 'badphilosopher/main.html')

class SeminarsAnswerListView(ListView):
    """ Семинары. Список ответов """
    model = Seminars
    paginate_by = 10
    queryset = Seminars.objects.order_by('number').all()
    context_object_name = 'achieves_obj'
    template_name = "badphilosopher/seminars_answer_list.html"

class SeminarsDetailedAnswerlView(DetailView):
    """ Семинары. Страница одного ответа """
    model = Seminars
    slug_field = "number"
    context_object_name = "answer"
    template_name = 'badphilosopher/detailed_answer.html'
