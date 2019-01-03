from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from django.conf import settings # debugging

# Create your views here.

def index(request) :
    print(settings.SOCIAL_AUTH_LOGIN_REDIRECT_URL)
    return render(request, 'authentication/index.html');
