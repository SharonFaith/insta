from django.shortcuts import render, redirect
from django.http import Http404, HttpResponse, HttpResponseRedirect
from .models import Image, Profile, UserFollowing, Comments, Like
import datetime as dt
from django.db import IntegrityError
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import UploadImageForm, UpdateProfileForm, CommentForm, FollowForm, LikeForm
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
   followed_users = UserFollowing.objects.all()
   #user_key = person being followed
   #following_user_id = user logged in who followed
   these_users = []
   
   for followed_user in followed_users:
      if followed_user.following_user_id == current_user :
         these_users.insert(0, followed_user)

   print(these_users)

   photos = Image.objects.all().order_by('-id')

  

   

   return render(request, 'index.html', {'photos': photos, 'users': these_users, 'all_users': users, 'current_user':current_user})
   


@login_required(login_url='/accounts/login')
def profile(request, id):
  
   users = User.objects.all()
   followed_users = UserFollowing.objects.all()
   #user_key = person being followed
   #following_user_id = user logged in who followed
   
      #if followed_user.following_user_id == current_user :
         

   
   logged_user = request.user
   current_user = User.objects.filter(id = id).first()
   
   followers = current_user.followers.all()

   current_follower = None
   print(followers)

   for follower in followers:
      if follower.user_key == logged_user:
         print(follower)
         current_follower = follower

   


   
  
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

  
   try:
      if request.method == 'POST':
         form = FollowForm(request.POST)
         formtrue = False

         if form.is_valid():
            userfollowing = form.save(commit=False)
            userfollowing.user_key = current_user
            userfollowing.following_user_id = logged_user
            
            userfollowing.save()
            phrase = f'You are following {current_user}'
         
      else:
         form = FollowForm()
         formtrue = True
         phrase = ''
   except IntegrityError as e:
         phrase = 'You cannot follow a user twice'



   print(UserFollowing.objects.all())

   photos = Image.objects.all().order_by('-id')
   pics = 'pics'
   
   return render(request, 'profile/profile.html', {'user_profile': current_profile, 'photos': photos, 'current_user':current_user, 'pics':pics, 'form': form, 'phrase':phrase, 'current_follower':current_follower, 'formtrue':formtrue })


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
   current_user = request.user

   pic = Image.objects.filter(id = image_id).first()
   numberoflikes = pic.numlikes.all().count()
   likemodel = Like.objects.all()
   print(likemodel)
   print(numberoflikes)
   the_comments = Comments.objects.all()
   comments = []
   phrase = ''
     
   try:
      if request.method == 'POST':
         form = LikeForm(request.POST)
         formtrue = False

         if form.is_valid():
            new_like = form.save(commit=False)
            new_like.user = current_user
            new_like.pic_image = pic
            
            new_like.save()
            #phrase = f'You are following {current_user}'
            numberoflikes = pic.numlikes.all().count()
         
      else:
         form = LikeForm()
         formtrue = True
         
   except IntegrityError as e:
      phrase = 'You have already liked this image '
      #return HttpResponse('<h1>You cannot like a picture twice</h1>')
   current_likes =   None
  
   likes = current_user.liked_posts.all()
   
   
   print(likes)

   for like in likes:
      print(like.pic_image)
      if like.pic_image.id == pic.id:
         print(like)
         current_likes = like

   print(current_likes)
   for comment in the_comments:
      if comment.an_image_id == pic.id:
         comments.append(comment)
   print(comments)

   return render(request, 'image.html', {'pic':pic, 'comments':comments, 'form':form, 'likes':numberoflikes, 'phrase':phrase, 'formtrue':formtrue, 'liked':current_likes})

@login_required(login_url='/accounts/login')
def single_image_comments(request):
   #pic = Image.objects.filter(id = image_id).first()

   #print(pic.comments)

   #return render(request, 'imageaftercomment.html', {'pic':pic})

   return redirect(single_image, image_id = single_image_id )


@login_required(login_url='/accounts/login')
def comments(request, id_image):
   current_user = request.user
   
         
   pic_id = id_image
   print(pic_id)
   if request.method == 'POST':
         formtrue = False
         form = CommentForm(request.POST)
         if form.is_valid():
            
            comment = form.save(commit=False)
            comment.an_image_id = id_image
            comment.save()
            print(comment)
            #image_id = None
            
            
         #return redirect(single_image_comments)
            #return HttpResponseRedirect(next)
            
   else:
        form = CommentForm()
        formtrue = True

   return render(request, 'comments.html', {'form':form, 'imageid':id_image, 'formtrue':formtrue})


# add post method in profile view function, impoert user_following model"



   