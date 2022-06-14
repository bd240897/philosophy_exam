from django.shortcuts import render
from django.views import View
from django.views.generic.edit import CreateView
from .forms import CommentForm


class CreateCommentView(CreateView):
    form_class = CommentForm
    success_url = "/contact/success"
    template_name = 'contact/comment_form.html'

class SuccessFormView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'contact/success_form.html')


