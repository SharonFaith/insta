from django.db import models
import datetime as dt

# Create your models here.



class Profile(models.Model):
#    profile_pic = models.ImageField(upload_to = 'uploads/', default = 'pics')
     bio = models.TextField()
#    uploader = maybe  to user model


class Image(models.Model):
#    image = models.ImageField(upload_to = 'uploads/', default = 'pics')
    image_name = models.CharField(max_length=60)
    image_caption = models.TextField()
    profile_key = models.ForeignKey(Profile, on_delete=models.CASCADE)
    likes = models.IntegerField()
    comments = models.TextField()

    upload_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.image_name

   