from django.urls import path
from django.urls import reverse

from . import views

app_name = "deck"

urlpatterns = [
    path('', views.index, name='index'),
    path('question/add/', views.question_add, name = 'question_add'),
    path('question/addanswer/<int:question_id>/', views.question_add_answer, name = 'question_add_answer'),
    path('not_implemented', views.not_impemented, name = 'not_implmented')
]


