from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    """
    Custom User model extending Django's AbstractUser
    Adds additional fields like mobile number
    """
    mobile = models.CharField(max_length=15, blank=True, null=True)
    
    def __str__(self):
        return self.username

class Task(models.Model):
    """
    Task model representing tasks in the system
    """
    TASK_TYPES = [
        ('personal', 'Personal'),
        ('work', 'Work'),
        ('study', 'Study'),
        ('other', 'Other')
    ]

    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed')
    ]

    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(blank=True, null=True)
    task_type = models.CharField(max_length=20, choices=TASK_TYPES, default='other')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    
    # Many-to-many relationship with User
    assigned_users = models.ManyToManyField(User, related_name='tasks')

    def __str__(self):
        return self.name