from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from .forms import UserLoginForm, UserRegistration
from django.contrib import auth


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('data:favourite_list'))
    else:
        form = UserLoginForm()
    context = {"form": form}
    return render(request, 'users/login.html', context)


def register(request):
    if request.method == 'POST':
        form = UserRegistration(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:login'))
    form = UserRegistration()
    context = {'form': form}
    return render(request, 'users/register.html', context)


def log_out(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('users:login'))
