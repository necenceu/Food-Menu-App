from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Item

# Create your views here.

def index(request):
    item_list = Item.objects.all()
    page_name = 'Main - GoodTaste'
    context = {
        'item_list':item_list,
        'page_name':page_name,
    }
    return render(request, 'food/index.html', context)

def detail(request, item_id):
    item = Item.objects.get(pk=item_id)
    page_name = 'Buy ' + item.item_name + ' - GoodTaste'
    context = {
        'item':item,
        'page_name':page_name,
    }
    return render(request, 'food/detail.html', context)

def item(request):
    return HttpResponse('This is an item view')
    