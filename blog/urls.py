from django.urls import path
from . import render_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # ! Template Rendering URL Routes
    # ? These URL's render the templates for further user interactions
    path('', render_views.renderHome, name="home"),
    path('category/', render_views.renderCategory, name="category"),
    path('archive/', render_views.renderArchive, name="archive"),
    path('contact/', render_views.renderContact, name="contact"),
    path('posts/', render_views.renderPosts, name="posts"),
]
