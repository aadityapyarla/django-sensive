from django.shortcuts import render, redirect
from .models import Account
from django.contrib import messages
from django.contrib.auth import logout, login, authenticate
from .views import custom_login, custom_register, get_login_cookies, send_auth_token


def render_login(request):
    context = {}
    # ! Thoughts for client side form validation
    # ? Will think about the implementation later
    # * If any suggestion, feel free to make a pull request
    # if request.is_ajax():
    #     if request.method == 'POST':
    #         return custom_login(request)
    if request.method == 'POST':
        return custom_login(request)
    cookies = get_login_cookies(request, 'dksjfnsdkjfnsdf')
    if cookies is not False:
        context = {'email': cookies['email'], 'password': cookies['password']}
    return render(request, 'accounts/login.html', context)


def render_register(request):
    if request.method == 'POST':
        return custom_register(request)
    return render(request, 'accounts/register.html')


def render_profile(request):
    return render(request, 'accounts/profile.html')


def render_new_post(request):
    return render(request, 'accounts/new_post.html')

def render_update_profile(request):
    context = {}
    return render(request, 'accounts/update_profile.html')

def render_auth_token_sent(request):
    if request.method == 'POST':
        email = request.session['resend_email']
        auth_token = request.session['auth_token']
        send_auth_token(request, auth_token, email)

    return render(request, 'accounts/auth_token_sent.html')


def render_logout(request):
    logout(request)
    return redirect('home')


def verify_auth_token(request, auth_token):
    account = Account.objects.filter(auth_token=auth_token).first()
    if account.is_active:
        if account.is_verified:
            messages.info(request, "Your email was already verified")
            return redirect('home')
        else:
            account.is_verified = True
            account.save()
            messages.info(request, "Your email was successfully verified!")
            login(request, account)
            return redirect('home')
    else:
        messages.error(request, "Your account is disabled")
        return redirect('home')


def PasswordResetCompleteView(request):
    return redirect('login')
