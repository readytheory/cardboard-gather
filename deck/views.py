from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse



# Create your views here.

from .models import Card

from .forms import NewQuestionForm, AddAnswerForm


def not_impemented(request) :
    return HttpResponse("That isn't ready yet")

def index(request):
    return HttpResponse("Time to learn things!")

def question_add(request):
    if request.method == 'POST' :
        form = NewQuestionForm(request.POST)
        if form.is_valid():
            try:
                newq = Card()
                user_q = request.POST['question']
                newq.question_text = user_q
                print("question text is" ,  user_q)
                newq.save()
                return HttpResponseRedirect(reverse('deck:question_add_answer', args=[newq.id]))
            except:
                return HttpResponseRedirect("/error")
    else:
        form = NewQuestionForm()
        return render(request, 'deck/add_question.html', {'form': form})




def question_add_answer(request, question_id =0) :
    from .models import Card
    if request.method == 'POST' :
        return HttpResponseRedirect("url not_impemented")

    if(question_id == 0) :
        return HttpResponse("no question id?  Really?")
    try:
        c = Card.objects.get(id=question_id)
    except:
        return HttpResponse("error loading card")
    
    question_text = c.question_text
    return render(request, 'deck/add_answer.html', {'question_text': question_text})
    



