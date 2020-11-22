from django.shortcuts import render, redirect
from django.http import Http404, HttpResponse
from .models import Image, Profile
import datetime as dt
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import UploadImageForm
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
 #  print(profiles)
   current_profile = None

 #  print(current_user.id)

   for user_profile in profiles:
 #     print(profile.insta_user)
      if user_profile.insta_user == current_user:
         current_profile = user_profile

   print(current_profile)
   if current_profile == None:
      current_profile = Profile.objects.create(insta_user= current_user)


   photos = Image.objects.all()
   pics = 'pics'
   
   return render(request, 'profile/profile.html', {'user_profile': current_profile, 'photos': photos, 'current_user':current_user, 'pics':pics })


@login_required(login_url='/accounts/login')
def upload_image(request):

   current_user = request.user
   
   profiles = Profile.objects.all()
   print(profiles)
   current_profile = None

  # print(current_user.id)

   for user_profile in profiles:
  #    print(profile.insta_user)
      if user_profile.insta_user == current_user:
         current_profile = user_profile
      

   print(current_profile)

   if current_profile == None:
      current_profile = Profile.objects.create(insta_user= current_user)

   print(current_profile)

   if request.method == 'POST':
      form = UploadImageForm(request.POST, request.FILES)

      if form.is_valid():
         image = form.save(commit=False)
         image.profile_key = current_profile
         image.likes = 0
         image.comments=[]
         image.save()
      return redirect(profile)
   else:
      form = UploadImageForm()
   
   return render(request, 'profile/upload_image.html', {'form': form})