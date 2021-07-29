from django.shortcuts import redirect
from django.contrib import messages
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
