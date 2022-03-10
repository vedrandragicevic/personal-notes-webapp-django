from unicodedata import name
from django.urls import URLPattern
from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePage, name="homepage"),
    path('logout/', views.logoutUser, name="logout"),
    path('login/', views.loginUser, name='login')
]