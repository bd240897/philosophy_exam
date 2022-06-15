from django.urls import path
from .views import LectionsAnswerListView, LectionsDetailedAnswerlView, MainPagelView, SeminarsAnswerListView, \
    SeminarsDetailedAnswerlView, CreateCommentLection, CreateCommentSeminar
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', MainPagelView.as_view(), name='main_page'),

    path('lections_list/', LectionsAnswerListView.as_view(), name='lections_answer_list'),
    path('lections_answer/<int:slug>/', LectionsDetailedAnswerlView.as_view(), name='lections_detailed_answer'),
    path('comment_lection/<int:current_post>/', CreateCommentLection.as_view(extra_context={"massage" : "hello"}), name="create_comment_lection"),

    path('seminars_list/', SeminarsAnswerListView.as_view(), name='seminars_answer_list'),
    path('seminars_answer/<int:slug>/', SeminarsDetailedAnswerlView.as_view(), name='seminars_detailed_answer'),
    path('comment_seminar/<int:current_post>/', CreateCommentSeminar.as_view(), name="create_comment_seminar"),

]

