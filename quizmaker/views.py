from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import Quiz

import logging

import bleach

def not_implemented(request) :
    return HttpResponse("That isn't ready yet")

def add_quiz(req) :
    qname = bleach.clean(req.POST['quizname'])
    if Quiz.objects.filter(name=qname):
        raise ValueError("A quiz named {} already exists.  Try a different name".format(qname))

    new_quiz = Quiz()
    new_quiz.name = qname
    new_quiz.save()
    return new_quiz.id

def create_interactive(request):
    if request.method == 'POST' :
        try:
            new_quiz_id = add_quiz(request)
            return HttpResponseRedirect(reverse('quizmaker:quiz_add_cards_form', args=[new_quiz_id]))
        except Exception as e:
            return HttpResponse ("It didn't work\n{}".format(e))
    else:
        return render(request, 'quizmaker/newquiz.html', {})
        
def add_cards_to_quiz_form(request, quiz_id) :
    try:
        quizname = Quiz.objects.get(id=quiz_id).name
    except:
        return HttpResponse("Can't get quiz name for id {}".format(quiz_id))
    return render(request, 'quizmaker/add_cards_to_quiz.html', { 'quiz_name' : quizname })

    
                      
    
                                    
                                    
                                    
     


