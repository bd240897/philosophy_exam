from django.shortcuts import render
from django.views import View
from django.views.generic.edit import CreateView

from .models import Comment
from .forms import CommentForm
from .models import Comment


class CreateCommentView(CreateView):
    form_class = CommentForm
    # model = Comment
    # fields = ["name", "email", "website", "message"]
    success_url = "/contact/success"
    template_name = 'contact/comment_form.html'

class SuccessFormView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'contact/success_form.html')


