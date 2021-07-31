from django.urls import path
from . import render_views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    # ! Template Renderer URL Routes
    # ? These URL's render the templates for further user interactions
    path('login/', render_views.render_login, name="login"),
    path('custom_register/', render_views.render_register, name="custom_register"),
    path('profile/', render_views.render_profile, name="profile"),
    path('new_post/', render_views.render_new_post, name="new_post"),

    # ! Data Processing URL Routes
    # ? These URL's don't render, instead they process the given data and redirects the user
    path('logout/', render_views.render_logout, name="logout"),
    path('auth_token_sent/', render_views.render_auth_token_sent, name="auth_token_sent"),
    path('auth_token_verify/<auth_token>/', render_views.verify_auth_token, name="auth_token_sent"),

    # ! Password Reset Email Routes
    # ? These URL's are provided by Django for Password Reset functionality, they do render the templates automatically
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="accounts/reset_pass.html"), name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="accounts/reset_pass_sent.html"), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="accounts/reset_pass_confirm.html"), name="password_reset_confirm"),
    path('reset_password_complete/', render_views.PasswordResetCompleteView, name="password_reset_complete"),
]
