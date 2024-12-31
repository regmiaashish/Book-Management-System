from django.urls import path
from user.views import create_user

from django.contrib.auth import views as auth_views

urlpatterns = [
    path("login/",auth_views.LoginView.as_view(template_name="create/login.html"),),
    path('register',create_user,name='create'),
]
