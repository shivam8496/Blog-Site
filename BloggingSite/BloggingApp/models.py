from email.policy import default
from operator import truediv
from django.db import models
from datetime import datetime

# Create your models here.
class post (models.Model):
    title = models.CharField(max_length=100)
    body =   models.CharField(max_length=100000)
    createdAt = models.DateTimeField(default = datetime.now,blank=True)