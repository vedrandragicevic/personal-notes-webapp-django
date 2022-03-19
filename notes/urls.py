from django.urls import path
from . import views


urlpatterns = [
    path('view-notes/', views.notes, name="mynotes"),
    path('view-completed-notes/', views.completed_notes, name="completed-notes"),
    path('track-note/<str:pk>', views.track_note, name="track-note"),
    path('view-notes/<str:pk>', views.update_completed_flag, name="updatenote"),
    path('delete-note/<str:pk>', views.delete_note, name="delete-note")
]
