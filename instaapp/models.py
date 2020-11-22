from django.db import models
import datetime as dt
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import User

# Create your models here.



class Profile(models.Model):
    profile_pic = models.ImageField(upload_to = 'uploads/', default = 'pics')
    bio = models.TextField()
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
    image = models.ImageField(upload_to = 'uploads/', default = 'pics')
    image_name = models.CharField(max_length=60)
    image_caption = models.TextField()
    profile_key = models.ForeignKey(Profile, on_delete=models.CASCADE)
    likes = models.IntegerField()
    comments = ArrayField(ArrayField(models.TextField()))

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