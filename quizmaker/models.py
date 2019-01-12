from django.db import models

class Quiz(models.Model) :
    def __str(self) :
        return "Quiz: {}".format (self.name)

    name = models.CharField(max_length=400)

