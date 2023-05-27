from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Item

# Create your views here.

def index(request):
    item_list = Item.objects.all()
    main_page_name = 'Good Taste'
    context = {
        'item_list':item_list,
        'main_page':main_page_name,
    }
    return render(request, 'food/index.html', context)

def detail(request, item_id):
    item = Item.objects.get(pk=item_id)
    context = {
        'item':item
    }
    return render(request, 'food/detail.html', context)

def item(request):
    return HttpResponse('This is a item view')
    