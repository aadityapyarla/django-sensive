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

    # ! Data Processing URL Routes
    # ? These URL's don't render, instead they process the given data and redirects the user
    path('logout/', render_views.renderLogout, name="logout"),
    path('auth_token_sent/', render_views.renderAuthTokenSent, name="auth_token_sent"),
    path('auth_token_verify/<auth_token>/', render_views.verifyAuthToken, name="auth_token_sent"),
]
