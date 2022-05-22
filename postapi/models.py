from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.


class Post(models.Model):

    post = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, default=None)
