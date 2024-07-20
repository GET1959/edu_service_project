from django.urls import path

from quiz.apps import QuizConfig
from quiz.views import Quiz, RandomQuestion, QuizQuestion, CreateAnswer

app_name = QuizConfig.name

urlpatterns = [
    path('', Quiz.as_view(), name='quiz'),
    path('r/<str:topic>/', RandomQuestion.as_view(), name='random'),
    path('q/<str:topic>/', QuizQuestion.as_view(), name='question'),
    path('test/<int:pk>/', CreateAnswer.as_view(), name='test'),
]
