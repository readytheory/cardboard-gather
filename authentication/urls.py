from django.urls import path, re_path
from django.urls import reverse

from . import views

app_name = "authenticaion"

urlpatterns = [
    path('', views.index, name='index'),
    ]
