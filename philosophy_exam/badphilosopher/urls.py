from django.urls import path
from .views import LectionsAnswerListView, LectionsDetailedAnswerlView, MainPagelView, SeminarsAnswerListView, \
    SeminarsDetailedAnswerlView, CreateCommentLection, CreateCommentSeminar
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', MainPagelView.as_view(), name='main_page'),

    path('lections/list/', LectionsAnswerListView.as_view(), name='lections_answer_list'),
    path('lections/answer/<int:slug>/', LectionsDetailedAnswerlView.as_view(), name='lections_detailed_answer'),
    path('lections/comment/<int:current_post>/', CreateCommentLection.as_view(extra_context={"massage" : "hello"}), name="create_comment_lection"),

    path('seminars/list/', SeminarsAnswerListView.as_view(), name='seminars_answer_list'),
    path('seminars/answer/<int:slug>/', SeminarsDetailedAnswerlView.as_view(), name='seminars_detailed_answer'),
    path('seminars/comment/<int:current_post>/', CreateCommentSeminar.as_view(), name="create_comment_seminar"),

]

