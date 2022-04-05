from unicodedata import name
from xml.etree.ElementInclude import include
from django.urls import path, include
from . import views


urlpatterns = [
    path('view-notes/', views.notes, name="mynotes"),
    path('view-completed-notes/', views.completed_notes, name="completed-notes"),
    path('track-note/<str:pk>', views.track_note, name="track-note"),
    path('view-notes/<str:pk>', views.update_completed_flag, name="updatenote"),
    path('delete-note/<str:pk>', views.delete_note, name="delete-note"),
    path('create-note/', views.create_note, name="create-note"),
    path('single-note/<str:pk>', views.single_note, name="single-note"),
    path('edit-single-note/<str:pk>/', views.edit_single_note, name="edit-single-note")
]
