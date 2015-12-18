from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.shortcuts import redirect
from dashboard.models import Document
from dashboard.forms import DocumentForm
from django.shortcuts import redirect
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from .models import Document
#from myproject.myapp.models import Document
#from myproject.myapp.forms import DocumentForm
from .forms import DocumentForm


@login_required
def dashboard(request):
    model = Document, User
    document = Document.objects.filter(user_id = request.user.id)[:1]
    return render(request, "tag.html", {'document':document})

@login_required
def profiles(request):
    model = Document, User
    document = Document.objects.filter(user_id = request.user.id)[:1]
    return render(request, "profil.html", {'document':document})



def edit(request):
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES )
        if form.is_valid():
            newdoc = Document(user=request.user, docfile = request.FILES['docfile'], firstname = request.POST['firstname'], lastname = request.POST['lastname'], address = request.POST['address'],)
            newdoc.save()

            # Redirect to the document list after POST
            return redirect('dashboard.views.profiles')
    else:
        form = DocumentForm() # A empty, unbound form

   # Load documents for the list page
    document = Document.objects.filter(user_id = request.user.id)[:1]
   

    # Render list page with the documents and the form
    return render_to_response(
        'dashboard/list.html',
        {'document': document, 'form': form},
        context_instance=RequestContext(request)
    )

def profile_edit(request, pk):
    newdoc = get_object_or_404(Document, pk=pk)
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES, instance=newdoc )
        if form.is_valid():
            newdoc = Document(user=request.user, docfile = request.FILES['docfile'], firstname = request.POST['firstname'], lastname = request.POST['lastname'], address = request.POST['address'],)
            newdoc.save()

            # Redirect to the document list after POST
            return redirect('dashboard.views.profiles', pk=newdoc.pk)
    else:
        form = DocumentForm() # A empty, unbound form

   # Load documents for the list page
    document = Document.objects.filter(user_id = request.user.id)
   

    # Render list page with the documents and the form
    return render_to_response(
        'dashboard/list.html',
        {'document': document, 'form': form},
        context_instance=RequestContext(request)
    )

	
def new(request):
    model = Document, User
    document = Document.objects.filter(user_id = request.user.id)
    return render(request, 'dashboard/new.html', {'document': document})



