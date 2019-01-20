from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import Quiz, CardOnQuiz

from deck.models  import Card

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

def cards_on_quiz(quiz_id_sought) :
    '''Return dict of cardid:question_text on the given quiz, empty if none'''
    
    cards= CardOnQuiz.objects.filter(quiz_id=quiz_id_sought)
    retval = {}
    for card in cards:
       retval[card.id] = card.question_text
    return retval
    
def add_cards_to_quiz_form(request, quiz_id) :
    quizdata = {}
    try:
        quizname = Quiz.objects.get(id=quiz_id).name
    except:
        return HttpResponse("Can't get quiz name for id {}".format(quiz_id))
    quizdata['quiz_name'] = quizname
    quizdata['quiz_id'] = quiz_id

    quiz_cards=cards_on_quiz(quiz_id)
    
    recents = Card.objects.all().order_by('-id')[:25]
    
    cardpool = []
    for card in recents:
        cardpool.append({'id': card.id, 'question_text': card.question_text})
    quizdata['cardpool'] = cardpool
    quizdata['cards_on_quiz'] = quiz_cards
    return render(request, 'quizmaker/add_cards_to_quiz.html', quizdata)

def update_from_interactive_form(request):
    if request.method == 'POST' :
        postkeys = [k for k in request.POST.keys() if k.startswith("card_db_")]
        try:
            quiz_id = request.POST.get("quiz_id")
        except Exception:
            return HttpResponseRedirect("error_getting_key_id")
        for kstring in postkeys:
            card_id = None
            try:
                card_id= kstring.split('_')[2] #because each one is like card_db_252, and we want just the 252
            except:
                pass
            try:
#                import pdb; pdb.set_trace()
                coq = CardOnQuiz()
                coq.quiz = Quiz.objects.get(id =quiz_id)
                coq.card = Card.objects.get(id = card_id)
                coq.save()
            except:
                return HttpResponseRedirect("error_saving_cardquizrel")
            return HttpResponseRedirect("did it")
    else:
        return("only post")
