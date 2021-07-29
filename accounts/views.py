from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from .models import Account
from django.core.mail import send_mail


def send_auth_token(request, auth_token, email):
    request.session.set_expiry(0)
    request.session['resend_email'] = email
    request.session['auth_token'] = auth_token
    subject = 'Here is your link for Sensive.com'
    message = f'Click on the link to verify your account => http://{request.get_host()}/accounts/auth_token_verify/{auth_token}'
    send_mail(subject=subject, from_email=email, message=message, recipient_list=[email], fail_silently=False)
    return redirect('auth_token_sent')


def get_login_cookies(request, salt):
    try:
        cookies = {
            'email': request.get_signed_cookie('email', salt=salt),
            'password': request.get_signed_cookie('password', salt=salt)
        }
        return cookies
    except:
        return False


def register(request):
    username = request.POST.get('username')
    email = request.POST.get('email')
    password = request.POST.get('password')
    confirm_password = request.POST.get('confirm-password')

    if password == confirm_password:
        if Account.objects.filter(username=username):
            messages.error(request, "Your username is already taken")
            return redirect('register')
        if Account.objects.filter(email=email):
            messages.error(request, "Your email is already taken")
            return redirect('register')
        user = Account.objects.create_user(email=email, username=username, password=password)
        return send_auth_token(request, str(user), email)

    else:
        messages.error(request, "Your passwords don't match each other")
        return redirect('register')


def custom_login(request):
    email = request.POST.get('email')
    password = request.POST.get('password')
    remmember = request.POST.get('remmember')
    account = Account.objects.filter(email=email).first()
    if account:
        if account.is_verified:
            if account.is_active:
                user = authenticate(request, username=email, password=password)
                if user is not None:
                    response = redirect('home')
                    if remmember == 'on':
                        response.set_signed_cookie('email', email, salt="dksjfnsdkjfnsdf", max_age=86400)
                        response.set_signed_cookie('password', password, salt="dksjfnsdkjfnsdf", max_age=86400)
                        login(request, user)
                        messages.success(request, "You are successfully logged in")
                        return response
                    if remmember is None and 'email' in request.COOKIES and 'password' in request.COOKIES:
                        response.delete_cookie('email')
                        response.delete_cookie('password')
                        login(request, user)
                        messages.success(request, "You are successfully logged in")
                        return response
                    login(request, user)
                    messages.success(request, "You are successfully logged in")
                    return response
                else:
                    messages.error(request, "Invalid Credentials")
                    return redirect('login')
            else:
                messages.info(request, "Your account is disabled")
                return redirect('login')
        else:
            user = authenticate(request, username=email, password=password)
            if user is not None:
                return send_auth_token(request, account.auth_token, account.email)
            else:
                messages.error(request, "Invalid Credentials")
                return redirect('login')
    else:
        messages.error(request, "Your account doesn't exists, please create on to continue")
        return redirect('login')
