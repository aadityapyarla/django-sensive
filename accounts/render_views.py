from django.shortcuts import render, redirect


def renderLogin(request):
    return render(request, 'accounts/login.html')


def renderRegister(request):
    return render(request, 'accounts/register.html')


def renderProfile(request):
    return render(request, 'accounts/profile.html')


def renderNewPost(request):
    return render(request, 'accounts/new_post.html')
