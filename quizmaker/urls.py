from django.urls import path, re_path
from django.urls import reverse

from . import views

app_name = "quizmaker"

urlpatterns = [
    re_path('^create/$', views.create_interactive, name='quiz_create_from_form_data'),
]


