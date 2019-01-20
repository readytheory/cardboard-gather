from django.db import models
from deck.models import Card

class Quiz(models.Model):
    def __str(self) :
        return "Quiz: {}".format (self.name)

    name = models.CharField(max_length=400)

class CardOnQuiz(models.Model):
    def __str(self):
        return "relation between one quiz and one cards"

    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    
    


