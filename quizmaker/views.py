from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


import logging

import bleach



def not_implemented(request) :
    return HttpResponse("That isn't ready yet")

def create_interactive(request):
    return render(request, 'quizmaker/newquiz.html', {})

