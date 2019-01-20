from django.urls import path, re_path
from django.urls import reverse

from . import views

app_name = "quizmaker"

urlpatterns = [
    re_path('^create/$', views.create_interactive, name='quiz_create_from_form_data'),
    path('add_cards_to_quiz/<int:quiz_id>', views.add_cards_to_quiz_form, name='quiz_add_cards_form'),
    path('update_from_interactive_form', views.update_from_interactive_form, name='update_from_interactive_form'),
]


