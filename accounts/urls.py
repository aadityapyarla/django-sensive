from django.urls import path
from . import render_views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    # ! Template Renderer URL Routes
    # ? These URL's render the templates for further user interactions
    path('login/', render_views.renderLogin, name="login"),
    path('register/', render_views.renderRegister, name="register"),
    path('profile/', render_views.renderProfile, name="profile"),
    path('new_post/', render_views.renderNewPost, name="new_post"),
]
