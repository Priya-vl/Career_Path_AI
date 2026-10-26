from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    ROLE_CHOICES = [
        ("student", "Student"), ("parent", "Parent"), ("admin", "Administrator"),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default="student")
    current_class = models.PositiveSmallIntegerField(null=True, blank=True)
    state = models.CharField(max_length=100, blank=True)
    board = models.CharField(max_length=100, blank=True)
    preferred_language = models.CharField(max_length=30, default="English")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} ({self.role})"
