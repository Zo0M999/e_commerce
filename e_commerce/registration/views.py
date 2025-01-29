from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import SignUpForm, UpdateUserForm, UserInfoForm, CheckOldPasswordForm, ChangePasswordForm
from .models import Profile
import json
from cart.cart import Cart


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)

            profile = Profile.objects.get(user__id=request.user.id)
            data = profile.cart_data
            if data:
                cart_data = json.loads(data)
                cart = Cart(request)
                cart.add_from_db(cart_data)

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
            return redirect('registration:add_info')
        else:
            for error in list(form.errors.values()):
                messages.error(request, error)
            return redirect('registration:register')

    return render(request, 'registration/register.html', context={
        'title': 'Register',
        'form': form,
    })

def profile(request):
    if request.user.is_authenticated:
        user = User.objects.get(id=request.user.id)
        return render(request, 'registration/profile.html', context={
            'user': user,
        })
    else:
        return redirect('registration:login')

def edit_profile(request):
    if request.user.is_authenticated:
        curr_user = User.objects.get(id=request.user.id)
        user_form = UpdateUserForm(request.POST or None, instance=curr_user)
        if user_form.is_valid():
            user_form.save()
            login(request, curr_user)
            messages.success(request, 'Profile updated successfully!')
            return redirect('registration:profile')

        return render(request, 'registration/edit_profile.html', context={
            'title': 'Edit profile',
            'user_form': user_form,
        })
    else:
        messages.error(request, 'You need to be logged in to update your profile!')
        return redirect('store:home')

def add_info(request):
    if request.user.is_authenticated:
        curr_user = Profile.objects.get(user__id=request.user.id)
        info_form = UserInfoForm(request.POST or None, request.FILES or None, instance=curr_user)
        if info_form.is_valid():
            info_form.save()
            messages.success(request, 'Profile information updated successfully!')
            return redirect('registration:profile')

        return render(request, 'registration/add_info.html', context={
            'title': 'Add Info',
            'info_form': info_form,
        })
    else:
        messages.error(request, 'You need to be logged in to add profile information!')
        return redirect('registration:add_info')

def check_old_password(request):
    form = CheckOldPasswordForm()
    if request.user.is_authenticated:
        curr_user = request.user
        if request.method == 'POST':
            old_password = request.POST.get('old_password')
            if curr_user.check_password(old_password):
                return redirect('registration:update_password')
            else:
                messages.error(request, 'Invalid password!')
                return redirect('registration:check_old_password')

    return render(request, 'registration/check_old_password.html', context={
        'title': 'Check old password',
        'form': form,
    })

def update_password(request):
    if request.user.is_authenticated:
        curr_user = request.user
        if request.method == 'POST':
            form = ChangePasswordForm(curr_user, request.POST)
            if form.is_valid():
                form.save()
                login(request, curr_user)
                messages.success(request, 'Password updated successfully!')
                return redirect('registration:profile')
            else:
                for error in list(form.errors.values()):
                    messages.error(request, error)
                return redirect('registration:update_password')
        else:
            form = ChangePasswordForm(request.user)
            return render(request, 'registration/update_password.html', context={
                'title': 'Update password',
                'form': form,
            })
    else:
        messages.error(request, 'You need to be logged in to update your password!')
        return redirect('store:home')
