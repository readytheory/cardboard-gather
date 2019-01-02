from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import Card
from .models import WrongAnswer, RightAnswer
from .forms import NewQuestionForm, AddAnswerForm
from .deck_util import login_string

def not_implemented(request) :
    return HttpResponse("That isn't ready yet")

def index(request):
    return HttpResponse("Time to learn things!")

def question_add(request, just_added = 0):
    if request.method == 'POST' :
        form = NewQuestionForm(request.POST)
        if form.is_valid():
            try:
                newq = Card()
                user_q = request.POST['question']
                newq.question_text = user_q
                print("question text is" ,  user_q)
                newq.save()
                return HttpResponseRedirect(reverse('deck:question_add_answer_get', args=[newq.id]))
            except:
                return HttpResponseRedirect("/error")
    else:
        form = NewQuestionForm()
        stat = login_string(request)
        tym = ''
        if int(just_added) > 0:
            tym = 'Thank you for adding that!... You can add another below'
        return render(request, 'deck/add_question.html', {'form': form, 
                                                          'login_stat': stat,
                                                          'thanks_message': tym,})


def question_add_answer(request, question_id =0) :
    
    if request.method == 'POST' :
        aaf = AddAnswerForm(request.POST)
        if aaf.is_valid():
            question_id = aaf.cleaned_data['question_id']
            try:
                parentCard = Card.objects.get(id=question_id)
            except:
                return(HttpResponse("Error getting parent card {}".format(question_id)))
            r = aaf.cleaned_data['right_answer']
            right_ans = RightAnswer()
            right_ans.question = parentCard
            right_ans.right_answer_text = r
            try:
                right_ans.save()
            except Exception as e:
                return HttpResponse( "failed trying to save right answer, {}".format(e))
             
            wrongs =[]
            for i in range(1,7) :
                wrong = aaf.cleaned_data['wrong' + str(i)]
                if wrong.strip() :
                    wrong_ans = WrongAnswer()
                    wrong_ans.question = parentCard
                    wrong_ans.wrong_answer_text = wrong
                    try:
                        wrong_ans.save()
                    except:
                        return(HttpResponse("Error saving wrong answer to database"))
            print ("calling redirect")
            return redirect('deck:question_add_another', just_added=1)
        else:
            print("aaf not valid")
            
    if(question_id == 0) :
        return HttpResponse("no question id?  Really?")
    try:
        c = Card.objects.get(id=question_id)
    except:
        return HttpResponse("error loading card")
    
    question_text = c.question_text
    stat= login_string(request)
    return render(request, 'deck/add_answer.html', {'question_text': question_text,
                                                    'question_id': question_id,
                                                    'login_stat': stat})

def baby_quiz(request):
    return HttpResponse("You are at the baby quiz")
    



