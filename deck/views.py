from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import Card
from .models import WrongAnswer, RightAnswer
from .forms import NewQuestionForm, AddAnswerForm
from . import deck_util as U

import logging

logger = logging.getLogger('django')


import bleach



def not_implemented(request) :
    return HttpResponse("That isn't ready yet")

def index(request):
    return HttpResponse("Time to learn things!")

def question_add(request, just_added = ''):
    if request.method == 'POST' :
        logger.info("entered post mod with just_added = {}".format(just_added))
        form = NewQuestionForm(request.POST)
        if form.is_valid():
            logger.info("Calling persist_question")
            new_q_id = U.persist_question(request, logger)
            return HttpResponseRedirect(reverse('deck:question_add_answer_get', args=[new_q_id]))
        else:
            return HttpResponse("Error validating your question, try again")


    else:
        form = NewQuestionForm()
        stat = U.login_string(request)
        tym = ''
        user_cards = None
        if just_added == 'thanks':
            tym = 'Thank you for adding that!... You can add another below'
            if request.user.is_authenticated:
                user_cards = U.cards_by_user(request.user)
            else:
                tym += "  Since you aren't logged in, your card went immediately to published status."
  
        return render(request, 'deck/add_question.html', {'form': form, 
                                                          'login_stat': stat,
                                                          'thanks_message': tym,
                                                          'your_cards': user_cards})



    
def question_add_answer(request, question_id =0) :
    
    if request.method == 'POST' :
        aaf = AddAnswerForm(request.POST)
        if aaf.is_valid():
            question_id = aaf.cleaned_data['question_id']
            try:
                parentCard = Card.objects.get(id=question_id)
            except:
                return(HttpResponse("Error getting parent card {}".format(question_id)))
            r = bleach.clean(aaf.cleaned_data['right_answer_text'])
            right_ans = RightAnswer()
            right_ans.question = parentCard
            right_ans.right_answer_text = r
            try:
                right_ans.save()
            except Exception as e:
                return HttpResponse( "failed trying to save right answer, {}".format(e))
             
            wrongs =[]
            for i in range(1,7) :
                wrong = bleach.clean(aaf.cleaned_data['wrong' + str(i)])
                if wrong.strip() :
                    wrong_ans = WrongAnswer()
                    wrong_ans.question = parentCard
                    wrong_ans.wrong_answer_text = wrong
                    try:
                        wrong_ans.save()
                    except:
                        return(HttpResponse("Error saving wrong answer to database"))
            print ("calling redirect")
            return redirect('deck:question_add_another', just_added='thanks')
        else:
            print("aaf not valid")
            print("here is the no-good request {}".format(request))
            
    if(question_id == 0) :
        return HttpResponse("no question id?  Really?")
    try:
        c = Card.objects.get(id=question_id)
    except:
        return HttpResponse("error loading card")
    
    question_text = c.question_text
    stat= U.login_string(request)
    return render(request, 'deck/add_answer.html', {'question_text': question_text,
                                                    'question_id': question_id,
                                                    'login_stat': stat})

def baby_quiz(request):
    return HttpResponse("You are at the baby quiz")
    



