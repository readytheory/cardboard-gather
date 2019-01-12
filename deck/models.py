from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Card(models.Model):

    def __str__(self) :
        return "Card: {}".format( self.question_text)

    question_text = models.CharField(max_length=200);
    usable = models.BooleanField(default = True)

    display_len = 45

    def display_text(self) :
        if len(self.question_text) > self.display_len - 2 :
            return self.question_text[:self.display_len] + '...'
        else :
            return self.question_text
    
    """ An question can be turned off, not available for selection,
by setting this field to true"""


class CardAuthor(models.Model) :
    card = models.ForeignKey(
        Card,
        on_delete=models.CASCADE)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE)
    
    


class WrongAnswer(models.Model):
    
    question = models.ForeignKey(Card, on_delete=models.CASCADE)
    wrong_answer_text = models.CharField(max_length = 200)
    usable = models.BooleanField(default = True)
    """ An answer can be turned off, not available for selection,
by setting this field to true"""

    def __str__(self) :
        return "Wrong answer for: " + str(self.question)

class RightAnswer(models.Model):
    question = models.ForeignKey(Card, on_delete=models.CASCADE)
    right_answer_text  = models.CharField(max_length = 200)
    usable = models.BooleanField(default = True)
    """ An answer can be turned off, not available for selection,
by setting this field to true"""

    def __str__(self):
        return "Correct answer for: " + str(self.question)
