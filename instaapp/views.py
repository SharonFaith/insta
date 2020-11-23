from django.shortcuts import render, redirect
from django.http import Http404, HttpResponse
from .models import Image, Profile
import datetime as dt
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import UploadImageForm, UpdateProfileForm, CommentForm
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

   photos = Image.objects.all().order_by('-id')

   return render(request, 'index.html', {'photos': photos, 'users': users})
   


@login_required(login_url='/accounts/login')
def profile(request, id):
   
  # current_user = request.user
   current_user = User.objects.filter(id = id).first()
   
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
      return redirect(profile, id = current_user.id)
   else:
      form = UploadImageForm()
   
   return render(request, 'profile/upload_image.html', {'form': form})



@login_required(login_url='/accounts/login')
def update_profile(request):

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
   #   return HttpResponse('Profile not created correctly')
      current_profile = Profile.objects.create(insta_user= current_user)

   print(current_profile)

   if request.method == 'POST':
      form = UpdateProfileForm(request.POST, request.FILES)

      if form.is_valid():
       #  new_pic = form.cleaned_data['profile_photo']
        # new_bio = form.cleaned_data['profile_bio']
        # print(current_profile.id)
         
        # Profile.objects.filter(id = current_profile.id).update(profile_pic = new_pic, bio = new_bio)
         image_profile = form.save(commit=False)
         fake_user = User.objects.create(username = 'fake-user2')
         image_profile.insta_user = fake_user
         image_profile.save()
         Profile.objects.filter(id = current_profile.id).update(profile_pic = image_profile.profile_pic, bio = image_profile.bio)

         fake_user.delete()
         image_profile.delete()
         


      return redirect(profile, id = current_user.id)
   else:
      form = UpdateProfileForm()
   
   return render(request, 'profile/update_profile.html', {'form': form})


#@login_required(login_url='/accounts/login')
def search_results(request):
   if 'uname' in request.GET and request.GET['uname']:
      search_term = request.GET.get('uname')
      searched_users = User.objects.filter(username__icontains= search_term)
     
      message = f'{search_term}'

      return render(request, 'search.html', {'message':message, 'searched_users':searched_users})

   else:
      message = 'You have not searched for any term'

      return render(request, 'search.html', {'message':message})


@login_required(login_url='/accounts/login')
def single_image(request, image_id):
   pic = Image.objects.filter(id = image_id).first()
   print(pic.comments)

   return render(request, 'image.html', {'pic':pic})



@login_required(login_url='/accounts/login')
def comments(request):
   current_user = request.user
   profil = Profile.objects.filter(insta_user=current_user).first()
   pic = Image.objects.filter(profile_key = profil).first()
   print(pic)
   pic_array = pic.comments

   if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment_body = form.cleaned_data['comment']
            pic_array.insert(0, comment_body)
 #           pic.save()
            print(pic.comments)
            Image.objects.filter(profile_key = profil).update(comments = pic_array)
            
            return redirect(single_image, id = pic.id)
            
   else:
        form = CommentForm()

   return render(request, 'comments.html', {'form':form, 'pic':pic})

