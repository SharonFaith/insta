from django.db import models
import datetime as dt
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import User

# Create your models here.



class Profile(models.Model):
    profile_pic = models.ImageField(upload_to = 'uploads/', default = 'pics', blank =True)
    bio = models.TextField(blank =True)
    insta_user = models.ForeignKey(User, on_delete=models.CASCADE, default = None)

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    @classmethod
    def update_profile(cls, id, updates):
        to_update = cls.objects.filter(id = id)
        to_update.update(bio = updates)

class Image(models.Model):
    image = models.ImageField(upload_to = 'uploads/', default = 'uploads/harp_b1l0RNq.jpeg')
    image_name = models.CharField(max_length=60)
    image_caption = models.TextField()
    profile_key = models.ForeignKey(Profile, on_delete=models.CASCADE)
    likes = models.IntegerField(blank =True)
    comments = ArrayField(ArrayField(models.TextField()), blank =True)

    upload_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.image_name

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()
   
    @classmethod
    def update_caption(cls, id, updates):
        to_update = cls.objects.filter(id = id)
        to_update.update(image_caption = updates)
        
##
class UserFollowing(models.Model):

    user_key = models.ForeignKey(User, on_delete=models.CASCADE, default = None, related_name='following')

    following_user_id = models.ForeignKey(User, on_delete=models.CASCADE, default = None, related_name='followers')

    class Meta:
        unique_together = ('user_key', 'following_user_id')

class Comments(models.Model):
    comment_body = models.TextField()
    an_image_id = models.IntegerField()