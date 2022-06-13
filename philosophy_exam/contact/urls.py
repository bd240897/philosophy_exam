from django.urls import path
from .views import CreateCommentView, SuccessFormView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', CreateCommentView.as_view(), name='comment_form'),
    path('success/', SuccessFormView.as_view(), name='success_form')
]

