# -*- coding: utf-8 -*-
from django.db import models
from django.views.generic import View, TemplateView
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from user_profile.models import UserProfile
from django.contrib.auth.models import User
from django.template import Context
from .forms import ProfileForm


@login_required

def profile(request):
    if request.method == "POST":
        avtar = ProfileForm(request.POST,request.FILES)
        if avtar.is_valid():
            profile = avtar.save(commit=False)
            profile.save()
       
            return redirect('/home/') 
    else:
        avtar = ProfileForm()
    return render(request, 'user_profile/profile1.html', {'avtar': avtar})   





