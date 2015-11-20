from django.shortcuts import render


def about(request):
	return render(request, "about.html", {})

def blank(request):
	return render(request, "blank.html", {})


def faq(request):
	return render(request, "faq.html", {})
