from pyexpat import model
from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
 

class Post(models.Model):
    Title = models.CharField(max_length=200)
    Text = models.TextField()
    Author = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    Created_date = models.DateTimeField(default= timezone.now)
    Published_date = models.DateTimeField()
# Create your models here.
