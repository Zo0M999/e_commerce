from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm

from bs4 import BeautifulSoup


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            messages.success(request, 'You have been logged in!')
            return redirect('store:home')
        else:
            messages.error(request, 'Invalid credentials!')
            return redirect('registration:login')

    return render(request, 'registration/login.html', context={
        'title': 'Login',
    })

def logout_user(request):
    logout(request)
    messages.success(request, 'You have been logged out!')
    return redirect('store:home')


def register_user(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, f'Account created for {username}!')
            return redirect('store:home')
        else:
            errors = form.errors
            for _, error in errors.items():
                soup = BeautifulSoup(str(error), 'html.parser')
                error_message = soup.find('ul', class_='errorlist').find('li').text
                messages.error(request, error_message)
            return redirect('registration:register')

    return render(request, 'registration/register.html', context={
        'title': 'Register',
        'form': form,
    })