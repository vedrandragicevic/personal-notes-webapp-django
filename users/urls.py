from unicodedata import name
from django.urls import URLPattern
from django.urls import path
from . import views

urlpatterns = [
    path('logout/', views.logoutUser, name="logout"),
    path('login/', views.loginUser, name='login'),
    path('', views.homePageRender, name="homepage"),
    path('register/', views.registerUser, name="register"),
]
    