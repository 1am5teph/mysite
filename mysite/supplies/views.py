from django.http import HttpResponse
from django.shortcuts import render

from .models import Item

def item_list(request):
    items = Item.objects.all()
    #output = ', '.join([str(item) for item in items])
    return render(request, 'supplies/item_list.html', {'items' : items})
