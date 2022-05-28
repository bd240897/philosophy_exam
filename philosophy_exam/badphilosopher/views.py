from django.shortcuts import render, get_object_or_404
from django.views import View
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import redirect
from .models import Lections


class AnswerListView(View):
    """ Список вопросов """

    def get(self, request, *args, **kwargs):
        # achieves = Lections.objects.order_by('number')
        # return render(request, 'bedphilosopher/main.html')
        #
        # achieves = get_object_or_404(Lections, number=1)

        achieves = Lections.objects.order_by('number').all()
        paginator = Paginator(achieves, 10)
        page_number = request.GET.get('page')
        achieves_obj  = paginator.get_page(page_number)
        return render(request, 'badphilosopher/answer_list.html', context={'achieves_obj': achieves_obj })

class DetailedAnswerlView(View):
    """ Страница одного ответа"""

    def get(self, request, slug, *args, **kwargs):
        answer = get_object_or_404(Lections, number=slug)
        return render(request, 'badphilosopher/detailed_answer.html', context={'answer': answer})

class MainPagelView(View):
    """ Страница одного ответа"""

    def get(self, request, *args, **kwargs):
        return render(request, 'badphilosopher/main.html')