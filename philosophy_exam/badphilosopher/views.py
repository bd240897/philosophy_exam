from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView, DetailView, CreateView

from .forms import CommentLectionForm, CommentSeminarForm
from .models import Lections, Seminars, CommentLection, CommentSeminar

# //////// ГЛАВНАЯ ////////

class MainPagelView(View):
    """Главная страница"""

    def get(self, request, *args, **kwargs):
        return render(request, 'badphilosopher/main.html')

# //////// ЛЕКЦИИ ////////


class LectionsAnswerListView(ListView):
    """ Список вопросов """
    model = Lections
    paginate_by = 10
    queryset = Lections.objects.order_by('number').all()
    context_object_name = 'achieves_obj'


class LectionsDetailedAnswerlView(DetailView):
    """ Страница одного ответа"""
    model = Lections
    slug_field = "number"
    context_object_name = "answer"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentLectionForm()
        return context


class CreateCommentLection(CreateView):
    model = CommentLection
    form_class = CommentLectionForm
    success_url = '/'
    template_name = 'badphilosopher/detailed_answer.html'

    def form_valid(self, form):
        current_post = self.kwargs.get('current_post')
        post = Lections.objects.get(number=current_post)
        form.instance.post = post
        self.object = form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return self.object.post.get_absolute_url()


# //////// СЕМИНАР ////////

class SeminarsAnswerListView(ListView):
    """ Семинары. Список ответов """
    model = Seminars
    paginate_by = 10
    queryset = Seminars.objects.order_by('number').all()
    context_object_name = 'achieves_obj'

class SeminarsDetailedAnswerlView(DetailView):
    """ Семинары. Страница одного ответа """
    model = Seminars
    slug_field = "number"
    context_object_name = "answer"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentSeminarForm()
        return context

class CreateCommentSeminar(CreateView):
    model = CommentSeminar
    form_class = CommentSeminarForm
    success_url = '/'
    template_name = 'badphilosopher/detailed_answer.html'

    def form_valid(self, form):
        current_post = self.kwargs.get('current_post')
        post = Seminars.objects.get(number=current_post)
        form.instance.post = post
        self.object = form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return self.object.post.get_absolute_url()
