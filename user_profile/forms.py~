#encoding:utf-8
#from .models import UserProfile
from django.contrib.auth.models import User
from django import forms
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import authenticate
from user_profile.models import UserProfile
from PIL import Image as PImage
from os.path import join as pjoin


class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ( 'avatar', 'twitter' )



