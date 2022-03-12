from django.db import models
import uuid
from users.models import Profile


class Note(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    note_title = models.CharField(max_length=400)
    note_data = models.TextField(null=True, blank=True)
    priority_type = (
        ('high', 'High Priority'),
        ('medium', 'Medium Priority'),
        ('low', 'Low Priority')
    )
    created = models.DateTimeField(auto_now_add=True)
    completed_flag = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)
    


    def __str__(self):
        return self.note_title