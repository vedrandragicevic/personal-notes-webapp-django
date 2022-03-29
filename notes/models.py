from django.db import models
import uuid
from users.models import Profile


class Note(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    note_title = models.CharField(max_length=400)
    note_data = models.TextField(null=True, blank=True)
    priority = (
        ('high', 'High Priority'),
        ('medium', 'Medium Priority'),
        ('low', 'Low Priority')
    )
    priority_type = models.CharField(max_length=50, choices=priority, default='low')
    created = models.DateTimeField(auto_now_add=True)
    completed_flag = models.BooleanField(default=False)
    owner = models.ForeignKey(Profile, null=True, blank=True, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.note_title

    
    class Meta:
        ordering = ['-created']
