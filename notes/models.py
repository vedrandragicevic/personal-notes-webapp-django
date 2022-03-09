from django.db import models
import uuid


# Create your models here.

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



    def __str__(self):
        return self.note_title