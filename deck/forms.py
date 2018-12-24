from django import forms

class NewQuestionForm(forms.Form):
    question = forms.CharField(label = "Question", max_length=200)

class AddAnswerForm(forms.Form):
    right_answer = forms.CharField(initial="Correct Answer")
    wrong1 = forms.CharField(required=True)
    wrong2 = forms.CharField(required=False)
    wrong3 = forms.CharField(required=False)
    wrong4 = forms.CharField(required=False)
    wrong5 = forms.CharField(required=False)
    wrong6 = forms.CharField(required=False)
    question_id = forms.IntegerField(required=True)
    
