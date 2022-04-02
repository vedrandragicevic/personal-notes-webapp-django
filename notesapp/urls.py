"""notesapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from re import template
from django.contrib import admin
from django.urls import path, include
# NEXT 2 IMPORTS HELP CREATE URLs FOR STATIC FILES
from django.conf import settings
from django.conf.urls.static import static
# CLASS BASED VIEWS
from django.contrib.auth import views as auth_views


# SEPERATE URLS INTO MULTIPLE MODULES BASED ON THE APP
urlpatterns = [
    path('admin/', admin.site.urls),
    path('notes/', include('notes.urls')),
    path('', include('users.urls')),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='password_reset.html'), name="password-reset"),
    path('password_reset_sent/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_sent.html'), name="password_reset_done"),
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_confirm.html"), name="password_reset_confirm"),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_complete.html"), name="password_reset_complete")
]


# CONFIGURE URLs FOR STATIC FILES
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
