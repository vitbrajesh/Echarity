from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import List_items1
from products.models import Product
from .forms import PostForm
from django import forms
from django.shortcuts import redirect
def post_list(request):
    posts = Product.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    return render(request, 'items/post_list.html', {'posts': posts})

def post_detail(request, pk):
	#event = Event.objects.get(pk=pk)
    
    post = get_object_or_404(Product, pk=pk)
    #post = List_items.objects.get(pk=pk)
    return render(request, 'items/post_detail.html', {'post': post})
  
#def post_new(request):
    #form = PostForm()
    #return render(request, 'items/post_edit.html', {'form': form})
	
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('items.views.post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'items/post_edit.html', {'form': form})
