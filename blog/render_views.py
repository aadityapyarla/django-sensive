from django.shortcuts import render
# Create your views here.


def renderHome(request):
    context = {}
    return render(request, 'blog/home.html', context)


def renderArchive(request):
    context = {}
    return render(request, 'blog/archive.html', context)


def renderCategory(request):
    context = {}
    return render(request, 'blog/category.html', context)


def renderContact(request):
    context = {}
    return render(request, 'blog/contact.html', context)


def renderPosts(request):
    context = {}
    return render(request, 'blog/posts.html', context)
