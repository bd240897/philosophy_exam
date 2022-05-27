from django.shortcuts import render, get_object_or_404
from django.views import View
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import redirect
from .models import lections


class IndexPage(View):
    """ Главная страница ТЕСТ """

    def get(self, request, *args, **kwargs):
        return render(request, 'bedphilosopher/index.html')

class MainPage(View):
    """ Главная страница """

    def get(self, request, *args, **kwargs):
        # achieves = lections.objects.order_by('number')
        # return render(request, 'bedphilosopher/main.html')
        #
        # achieves = get_object_or_404(lections, number=1)

        achieves = lections.objects.order_by('number').all()
        paginator = Paginator(achieves, 6)
        page_number = request.GET.get('page')
        achieves_obj  = paginator.get_page(page_number)
        return render(request, 'bedphilosopher/main.html', context={'achieves_obj': achieves_obj })

class AnswerDetailView(View):
    """ Страница поста"""

    def get(self, request, slug, *args, **kwargs):
        answer = get_object_or_404(lections, number=slug)
        return render(request, 'bedphilosopher/answer.html', context={'answer': answer})

