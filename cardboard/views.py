from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


def google_oauth2(request) :
    return HttpResponse("You logged in with google")

def index(request) :
    return HttpResponse("Index")
