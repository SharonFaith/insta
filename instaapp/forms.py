from django import forms
from .models import Image


class UploadImageForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['profile_key', 'likes', 'comments', 'upload_date']
        