from django.shortcuts import render, get_object_or_404
from django.views import View
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import redirect
from .models import Lections, Seminars


class LectionsAnswerListView(View):
    """ Список вопросов """

    def get(self, request, *args, **kwargs):
        achieves = Lections.objects.order_by('number').all()
        paginator = Paginator(achieves, 10)
        page_number = request.GET.get('page')
        achieves_obj  = paginator.get_page(page_number)
        return render(request, 'badphilosopher/lections_answer_list.html', context={'achieves_obj': achieves_obj})

class LectionsDetailedAnswerlView(View):
    """ Страница одного ответа"""

    def get(self, request, slug, *args, **kwargs):
        answer = get_object_or_404(Lections, number=slug)
        return render(request, 'badphilosopher/detailed_answer.html', context={'answer': answer})

class MainPagelView(View):
    """Главная страница"""

    def get(self, request, *args, **kwargs):
        return render(request, 'badphilosopher/main.html')

class SeminarsAnswerListView(View):
    """ Семинары. Список ответов """

    def get(self, request, *args, **kwargs):
        achieves = Seminars.objects.order_by('number').all()
        paginator = Paginator(achieves, 10)
        page_number = request.GET.get('page')
        achieves_obj = paginator.get_page(page_number)
        return render(request, 'badphilosopher/seminars_answer_list.html', context={'achieves_obj': achieves_obj})

class SeminarsDetailedAnswerlView(View):
    """ Семинары. Страница одного ответа """

    def get(self, request, slug, *args, **kwargs):
        answer = get_object_or_404(Seminars, number=slug)
        return render(request, 'badphilosopher/detailed_answer.html', context={'answer': answer})