from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def blank(request):
	return render(request, "blank.html", {})

def about(request):
	return render(request, "about.html", {})

def faq(request):
	return render(request, "faq.html", {})

def policy(request):
	return render(request, "policy.html", {})

def term(request):
	return render(request, "term.html", {})

def gallery(request):
	return render(request, "gallery.html", {})
