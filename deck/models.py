from django.db import models

# Create your models here.

class Card(models.Model):
    question_text = models.CharField(max_length=200);
    usable = models.BooleanField(default = True)
    """ An question can be turned off, not available for selection,
by setting this field to true"""



class WrongAnswer(models.Model):
    
    question = models.ForeignKey(Card, on_delete=models.CASCADE)
    wrong_answer = models.CharField(max_length = 200)
    usable = models.BooleanField(default = True)
    """ An answer can be turned off, not available for selection,
by setting this field to true"""

    def __str__(self) :
        return "Wrong: " + self.question

class RightAnswer(models.Model):
    question = models.ForeignKey(Card, on_delete=models.CASCADE)
    right_answer = models.CharField(max_length = 200)
    usable = models.BooleanField(default = True)
    """ An answer can be turned off, not available for selection,
by setting this field to true"""


    def __str__(self):
        return "Correct: " + self.question
    
