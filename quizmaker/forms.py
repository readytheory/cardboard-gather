from django import forms
from django.conf import settings

qname_max = settings.QUIZNAME_MAX

class NewQuizForm(forms.Form):
    name = forms.CharField(label = "Quiz name", max_length=qname_max)

class QuizConfigurationForm(forms.Form) :
    name = forms.CharField(label = "Quiz name", max_length=qname_max)

