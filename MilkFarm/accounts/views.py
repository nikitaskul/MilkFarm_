from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import UserLoginForm, UserRegisterForm, UserPasswordChangeForm, UserEmailChangeForm, \
    UserAdditionalInfoChangeForm, UserPaymentDetailsChangeForm, UserAddMoney


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home_page')
    else:
        form = UserLoginForm()
    return render(request, 'accounts/login.html', {'form': form})


def user_register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Вы успешно зарегистрировались')
            return redirect('home_page')
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = UserRegisterForm()
    return render(request, 'accounts/register.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('home_page')


@login_required
def user_account(request):
    return render(request, 'accounts/account.html')


@login_required
def user_account_change_form(request):
    if request.method == 'POST':
        form = UserEmailChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('accounts:account')
    else:
        form = UserEmailChangeForm(instance=request.user)
    return render(request, 'accounts/change_account.html', {'form': form})


@login_required
def user_additional_info_change_form(request):
    if request.method == 'POST':
        form = UserAdditionalInfoChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('accounts:account')
    else:
        form = UserAdditionalInfoChangeForm(instance=request.user)
    return render(request, 'accounts/change_account.html', {'form': form})


@login_required
def user_payment_details_change_form(request):
    if request.method == 'POST':
        form = UserPaymentDetailsChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('accounts:account')
    else:
        form = UserPaymentDetailsChangeForm(instance=request.user)
    return render(request, 'accounts/change_account.html', {'form': form})


@login_required
def add_money_to_user(request):
    if request.method == 'POST':
        form = UserAddMoney(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('accounts:account')
    else:
        form = UserAddMoney(instance=request.user)
    return render(request, 'accounts/change_account.html', {'form': form})


@login_required
def change_password(request):
    if request.method == 'POST':
        form = UserPasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('accounts:account')
    else:
        form = UserPasswordChangeForm(request.user)
    return render(request, 'accounts/change_password.html', {'form': form})
