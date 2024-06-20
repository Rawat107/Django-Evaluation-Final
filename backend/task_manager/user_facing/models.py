from django.db import models
from django.contrib.auth.models import User
from admin_facing.models import App
# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile/', null=True, blank=True)
    total_point = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    app = models.ForeignKey(App, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, default='pending')
    screenshot = models.ImageField(upload_to='tasks/', null=True, blank=True)

    def __str__(self):
        return f'{self.user.username} - {self.app.name}'
