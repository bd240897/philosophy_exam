from django.urls import path
from .views import LectionsAnswerListView, LectionsDetailedAnswerlView, MainPagelView, SeminarsAnswerListView, SeminarsDetailedAnswerlView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', MainPagelView.as_view(), name='main_page'),
    path('lections_list/', LectionsAnswerListView.as_view(), name='lections_answer_list'),
    path('lections_answer/<int:slug>/', LectionsDetailedAnswerlView.as_view(), name='lections_detailed_answer'),
    path('seminars_list/', SeminarsAnswerListView.as_view(), name='seminars_answer_list'),
    path('seminars_answer/<int:slug>/', SeminarsDetailedAnswerlView.as_view(), name='seminars_detailed_answer'),
]

