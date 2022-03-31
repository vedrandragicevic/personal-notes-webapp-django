from unicodedata import name
from django.urls import URLPattern
from django.urls import path
from . import views

urlpatterns = [
    path('logout/', views.logout_user, name="logout"),
    path('login/', views.login_user, name='login'),
    path('', views.home_page_render, name="homepage"),
    path('register/', views.register_user, name="register"),
    path('edit-account/', views.edit_account, name="edit-account")
]
    