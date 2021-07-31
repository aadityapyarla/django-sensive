from django.urls import path
from . import render_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # ! Template Rendering URL Routes
    # ? These URL's render the templates for further user interactions
    path('', render_views.render_home, name="home"),
    path('category/', render_views.render_category, name="category"),
    path('archive/', render_views.render_archive, name="archive"),
    path('contact/', render_views.render_contact, name="contact"),
    path('posts/', render_views.render_posts, name="posts"),
]
