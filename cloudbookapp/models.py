from django.contrib import admin
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# My model for my notes app foreignKey for private notes
class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, null=False, blank=False)
    content = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__ (self):
        return f'{self.title}'