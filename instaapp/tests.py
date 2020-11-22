from django.test import TestCase
from .models import Image, Profile
import datetime as dt
# Create your tests here.

class ProfileTestClass(TestCase):

    #set up method
    def setUp(self):
        self.new = Profile(bio = 'this is a bio')

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
        new2 = Profile(bio = 'profile bio number 2 ')
        new2.save_profile()

        new2.delete_profile()
        
        profiles = Profile.objects.all()

        self.assertTrue(len(profiles) == 1)

    def test_update_profile(self):
        self.new.save_profile()
        print(self.new.id)
        new2 = Profile(bio = 'profile bio number 2 ')
        new2.save_profile()

        Profile.update_profile(4, 'the new bio')
       
        self.assertEqual(Profile.objects.filter(id = 4).first().bio, 'the new bio')