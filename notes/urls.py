from django.urls import path
from . import views


urlpatterns = [
    path('view-notes/', views.notes, name="mynotes")
]
