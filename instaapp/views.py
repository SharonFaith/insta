from django.shortcuts import render, redirect
from django.http import Http404, HttpResponse

import datetime as dt
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import logout
# Create your views here.


def logout_view(request):
    logout(request)

    return redirect(index)


def welcome(request):

   return redirect(index)

def index(request):


    return render(request, 'index.html')