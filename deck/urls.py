from django.urls import path, re_path
from django.urls import reverse

from . import views

app_name = "deck"

urlpatterns = [
    path('', views.index, name='index'),
    path('question/add/', views.question_add, name = 'question_add'),
    re_path('question/add/(?P<just_added>thanks)/?$', views.question_add, name='question_add_another'),
    path('question/addanswer/<int:question_id>/', views.question_add_answer, name = 'question_add_answer_get'),
    path('question/addanswer/', views.question_add_answer, name = 'question_add_answer_post'),
    path('not_implemented', views.not_implemented, name = 'not_implemented'),
    path('quiz', views.baby_quiz, name='baby_quiz'),
]


