from .models import Card
from .models import WrongAnswer, RightAnswer, CardAuthor

import bleach

import logging


def login_string(request) :
    try:
        if request.user.username in ('',None) :
            return 'Not Logged In | DECK '
        else:
            return "{} | DECK ".format(request.user.username)
    except Exception as e :
        return 'Login N/A | DECK'
    
def persist_question(request, logger) :
    newq = Card()
    newq.question_text = bleach.clean(request.POST['question'])
    logger.info("saving question {}".format(newq.question_text))
    newq.save()
    question_id = newq.id
    user = request.user
    logger.info("deck_util: q id and uid {}/{}".format(question_id, user.id))
    
    if user.is_authenticated and user.id > 0 :
            a = CardAuthor()
            a.card = newq
            a.author = request.user
            a.save()

    return question_id
    
def cards_by_user(user, count=10) :
    '''Return a queryset of Card object made by a user'''
    authored_cards = Card.objects.filter(cardauthor__author=user).order_by('-id')
    return authored_cards

    

