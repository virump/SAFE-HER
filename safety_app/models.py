from django.contrib.auth.models import User
from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

# class Alert(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     location = models.CharField(max_length=255)
#     message = models.TextField()
#     timestamp = models.DateTimeField(auto_now_add=True)

class Location(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    latitude = models.FloatField()
    longitude = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)    

# tracking/models.py

class Alert(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    latitude = models.FloatField(default=0.0)
    longitude = models.FloatField(default=0.0)
    timestamp = models.DateTimeField(auto_now_add=True)
    emergency_type = models.CharField(max_length=50, choices=[('Emergency', 'Emergency'), ('Help', 'Help')], default='Emergency')
    custom_message = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'Alert from {self.user} at {self.timestamp}'
