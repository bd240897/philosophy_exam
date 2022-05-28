from django.urls import path
from .views import AnswerListView, DetailedAnswerlView, MainPagelView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', MainPagelView.as_view(), name='main_page'), # ГЛАВНАЯ
    path('list/', AnswerListView.as_view(), name='answer_list'), # ГЛАВНАЯ
    path('answer/<slug>/', DetailedAnswerlView.as_view(), name='detailed_answer'), # СТРАНИЦА ПОСТА
]
