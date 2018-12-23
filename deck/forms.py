from django import forms

class NewQuestionForm(forms.Form):
    question = forms.CharField(label = "Question", max_length=200)

class AddAnswerForm(forms.Form):
    right_answer = forms.CharField(initial="Correct Answer")



        
    
