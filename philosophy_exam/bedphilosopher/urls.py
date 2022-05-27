from django.urls import path
from .views import IndexPage, MainPage, AnswerDetailView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('index', IndexPage.as_view(), name='IndexPage'), # тест главной
    path('main', MainPage.as_view(), name='MainPage'), # ГЛАВНАЯ
    path('answer/<slug>/', AnswerDetailView.as_view(), name='answer_detail'), # СТРАНИЦА ПОСТА
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)