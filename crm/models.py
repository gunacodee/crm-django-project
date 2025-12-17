from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Account(models.Model):
    name = models.CharField(max_length=255)
    industry = models.CharField(max_length=150, blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
