
from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone 

User = get_user_model()

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField(max_length=255, default="")
    author = models.ForeignKey(User, on_delete=models.CASCADE, default="")
    created_date = models.DateTimeField(default="")
    published_date = models.DateTimeField(default="")

    def __str__(self):
        return self.title