from django.shortcuts import render, redirect
from django.http import Http404, HttpResponse

import datetime as dt
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.

def welcome(request):

   return redirect(index)

def index(request):


    return render(request, 'index.html')