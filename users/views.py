from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Create your views here.

def register(request):
    name = 'Register'

    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success(request, f'Welcome, {username}! You\'ve created an account.')
            form.save()
            return redirect('food:index')
    else:
        form = UserCreationForm()

    context = {
        'form':form,
        'page_name':name,
    }
    return render(request, 'users/register.html', context)