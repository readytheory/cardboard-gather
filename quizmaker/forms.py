from django import forms

class NewQuizForm(forms.Form):
    name = forms.CharField(label = "Quiz name", max_length=400)

