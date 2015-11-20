from django.shortcuts import render
from django.utils import timezone
from .models import Donatable_item
from django.shortcuts import render, get_object_or_404

def p_list(request):
    donatable_items = Donatable_item.objects.filter(date_created__lte=timezone.now()).order_by('date_Update')
    return render(request, 'item/item.html', {'donatable_items':donatable_items})

def p_detail(request, pk):
    donatable_item = get_object_or_404(Donatable_item , pk=pk)
    return render(request, 'item/p_detail.html', {'donatable_item':donatable_item})
