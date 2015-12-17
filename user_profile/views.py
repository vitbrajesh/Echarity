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
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response

@login_required

def profile(request):
    if request.method == "POST":
        avtar = ProfileForm(request.POST, request.FILES)
        if avtar.is_valid():
           profile = Avatar(user=request.user, image="", valid=False)
           profile.image.save("%s.jpg" % request.user.username, ContentFile(f.read()))
           profile.save()
            
       
           return redirect('dashboard.views.profile') 
    else:
        avtar = ProfileForm()

    return render_to_response(
        'user_profile/profile1.html',
        {'avtar': avtar},
        context_instance=RequestContext(request)
    )




