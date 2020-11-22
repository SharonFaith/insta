from django.shortcuts import render, redirect
from django.http import Http404, HttpResponse
from .models import Image, Profile
import datetime as dt
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.


def logout_view(request):
    logout(request)

    return redirect(index)


def welcome(request):

   return redirect(index)

@login_required(login_url='/accounts/login')
def index(request):
   users = User.objects.all()

   photos = Image.objects.all()

   return render(request, 'index.html', {'photos': photos, 'users': users})