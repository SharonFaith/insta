from django.contrib import admin
from .models import Image, Profile, UserFollowing, Comments, Like

# Register your models here.
admin.site.register(Profile)
admin.site.register(Image)

##
admin.site.register(UserFollowing)
admin.site.register(Comments)
admin.site.register(Like)
