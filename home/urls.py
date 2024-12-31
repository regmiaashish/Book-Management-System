from django.urls import path
from home.views import homepage
urlpatterns = [
    path("",homepage,name="homepage")
]