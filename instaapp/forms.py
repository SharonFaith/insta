from django import forms
from .models import Image, Profile


class UploadImageForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['profile_key', 'likes', 'comments', 'upload_date']
        
class UpdateProfileForm(forms.ModelForm):
     class Meta:
        model = Profile
        exclude = ['insta_user']
        
    #profile_photo = forms.ImageField(label='add photo')
    #profile_bio = forms.CharField(label='Bio')

class CommentForm(forms.Form):
    comment = forms.CharField(label = 'Add comment')