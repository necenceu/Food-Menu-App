from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import RegisterForm

# Create your views here.

# register function
def register(request):
    name = 'Register'

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success(request, f'Welcome, {username}! You\'ve created an account.')
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()

    context = {
        'form':form,
        'page_name':name,
    }
    return render(request, 'users/register.html', context)

# profile page only accessible for authorized users
@login_required
def profilePage(request):
    return render(request, 'users/profile.html', {'page_name':'Profile'})