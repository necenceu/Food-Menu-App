from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Item
from .forms import ItemForm

# Create your views here.

def index(request):
    item_list = Item.objects.all()
    page_name = 'Main - GoodTaste'
    context = {
        'item_list':item_list,
        'page_name':page_name,
    }
    return render(request, 'food/index.html', context)

class IndexClassView(ListView):
    model = Item
    template_name = 'food/index.html'
    context_object_name = 'item_list'

def detail(request, item_id):
    item = Item.objects.get(pk=item_id)
    page_name = 'Buy ' + item.item_name + ' - GoodTaste'
    context = {
        'item':item,
        'page_name':page_name,
    }
    return render(request, 'food/detail.html', context)

class FoodDetail(DetailView):
    model = Item
    template_name = 'food/detail.html'

@login_required
def add_item(request):
    form = ItemForm(request.POST or None)
    name = 'Add item'
    context = {
        'form':form,
        'page_name':name,
    }

    if form.is_valid():
        item_name = form.cleaned_data.get('item_name')
        messages.success(request, f'{item_name} has added to list!')
        form.save()
        return redirect('food:index')
    
    return render(request, 'food/item-form.html', context)

@login_required
def update_item(request, id):
    item = Item.objects.get(id = id)
    form = ItemForm(request.POST or None, instance=item)
    name = 'Update item'
    context = {
        'item':item,
        'form':form,
        'page_name':name,
    }

    if form.is_valid():
        item_name = form.cleaned_data.get('item_name')
        messages.success(request, f'{item_name} successfully updated!')
        form.save()
        return redirect('food:index')    
    return render(request, 'food/item-form.html', context)

@login_required
def delete_item(request, id):
    item = Item.objects.get(id = id)

    if request.method == 'POST':
        item_name = item.item_name
        messages.success(request, f'{item_name} successfully deleted!')
        item.delete()
        return redirect('food:index')
    
    return render(request, 'food/item-delete.html', {'item':item})

def item(request):
    return HttpResponse('This is an item view')
    