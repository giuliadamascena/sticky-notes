from django.db import models

class NoteManager(models.Manager):
    def active_notes(self):
        return self.filter(is_active=True)
    
class Note(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)  # Add this field if using active_notes manager

    # Assign the custom manager
    objects = NoteManager()

    def __str__(self):
        return self.title
