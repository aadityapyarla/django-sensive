from django.shortcuts import render, redirect
from .models import Account
from django.contrib import messages
from . views import register, send_auth_token
from django.contrib.auth import logout


def renderLogin(request):
    return render(request, 'accounts/login.html')


def renderRegister(request):
    if request.method == 'POST':
        return register(request)
    return render(request, 'accounts/register.html')


def renderProfile(request):
    return render(request, 'accounts/profile.html')


def renderNewPost(request):
    return render(request, 'accounts/new_post.html')


def renderAuthTokenSent(request):
    if request.method == 'POST':
        email = request.session['resend_email']
        auth_token = request.session['auth_token']
        send_auth_token(request, auth_token, email)

    return render(request, 'accounts/auth_token_sent.html')


def verifyAuthToken(request, auth_token):
    account = Account.objects.filter(auth_token=auth_token).first()
    if account.is_active:
        if account.is_verified:
            messages.info(request, "Your email was already verified")
            return redirect('home')
        else:
            account.is_verified = True
            account.save()
            messages.info(request, "Your email was successfully verified!")
            return redirect('home')
    else:
        messages.error(request, "Your account is disabled")
        return redirect('home')
