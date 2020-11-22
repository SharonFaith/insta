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
   current_user = request.user
   users = User.objects.all()

   photos = Image.objects.all()

   return render(request, 'index.html', {'photos': photos, 'users': users})
   


@login_required(login_url='/accounts/login')
def profile(request):

   current_user = request.user
   
   profiles = Profile.objects.all()
   print(profiles)
   current_profile = None

   print(current_user.id)

   for profile in profiles:
      print(profile.insta_user)
      if profile.insta_user == current_user:
         current_profile = profile

   print(current_profile)
   photos = Image.objects.all()
   #user_photos = []

   #for photo in photos:
    #  if current_profile.id == photo.profile_key:
     #    user_photos.insert(0, photo)
   
   return render(request, 'profile/profile.html', {'user_profile': current_profile, 'photos': photos, 'current_user':current_user })