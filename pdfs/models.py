from django.db import models
from django.contrib.auth.models import User
import os

class Books(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to='', max_length=2000)

    def __str__(self):
        return self.title
