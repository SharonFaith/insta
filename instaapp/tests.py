from django.test import TestCase
from .models import Image, Profile
import datetime as dt
from django.contrib.auth.models import User
# Create your tests here.

class ProfileTestClass(TestCase):

    #set up method
    def setUp(self):
        self.user1 = User(username = 'a-user')
        self.user1.save()
        self.new = Profile(bio = 'this is a bio', insta_user = self.user1)

  #  def tearDown(self):
    #    Profile.objects.all().delete()
        
    
    def test_instance(self):

        self.assertTrue(isinstance(self.new, Profile))
    
    def test_save_profile(self):

        self.new.save_profile()
        profiles = Profile.objects.all()

        self.assertTrue(len(profiles) > 0)

    def test_delete_profile(self):
        self.new.save_profile()
        new2 = Profile(bio = 'profile bio number 2 ', insta_user = self.user1)
        new2.save_profile()

        new2.delete_profile()
        
        profiles = Profile.objects.all()

        self.assertTrue(len(profiles) == 1)

    def test_update_profile(self):
        self.new.save_profile()
        print(self.new.id)
        new2 = Profile(bio = 'profile bio number 2 ',  insta_user = self.user1)
        new2.save_profile()

        Profile.update_profile(8, 'the new bio')
       
        self.assertEqual(Profile.objects.filter(id = 8).first().bio, 'the new bio')

class ImageTestClass(TestCase):

    def setUp(self):
        # Creating a profile and saving it
        self.user1 = User(username = 'a-user')
        self.user1.save()
        self.new = Profile(bio = 'a bio',  insta_user = self.user1)
        self.new.save_profile()

    
       

        #creating instance of image
        self.pic = Image(image_name = 'brown', image_caption= 'A brown picture', profile_key = self.new, likes = 2, comments = ['hello', 'how are you'])
        print(self.pic.comments)



    def tearDown(self):
        
        Profile.objects.all().delete()
        Image.objects.all().delete()

    def test_instance(self):

        self.assertTrue(isinstance(self.pic, Image))

    def test_save_image(self):
        self.pic.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)

    def test_delete_image(self):
        
        self.pic.save_image()
        image2 = Image(image_name = 'bread', image_caption= 'A  picture', profile_key = self.new, likes = 3, comments = ['hey', 'there'])
        image2.save_image()
        print(image2.profile_key.id)
        image2.delete_image()
        
        images = Image.objects.all()

        self.assertTrue(len(images) == 1)
        

    def test_update_caption(self):

        self.pic.save_image()
        image2 = Image(image_name = 'bread', image_caption= 'A  picture', profile_key = self.new, likes = 3, comments = ['hey', 'there'])
        image2.save_image()
        print(self.pic.id)
        Image.update_caption(4, 'Bread is nice')
    
       
        self.assertEqual(Image.objects.filter(id = 4).first().image_caption, 'Bread is nice')

