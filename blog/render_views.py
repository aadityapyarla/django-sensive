from django.shortcuts import render


# Create your views here.


def render_home(request):
    context = {}
    return render(request, 'blog/home.html', context)


def render_archive(request):
    context = {}
    return render(request, 'blog/archive.html', context)


def render_category(request):
    context = {}
    return render(request, 'blog/category.html', context)


def render_contact(request):
    context = {}
    return render(request, 'blog/contact.html', context)


def render_posts(request):
    context = {}
    return render(request, 'blog/posts.html', context)
