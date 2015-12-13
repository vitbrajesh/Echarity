from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from django.http import HttpResponse
from django.shortcuts import render_to_response

from django.forms import ModelForm


@login_required
def dashboard(request):
	return render(request, "tag.html", {})

@login_required
def profiles(request):
	return render(request, "profil.html", {})


