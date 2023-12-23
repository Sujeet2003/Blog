from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
import datetime

# Create your models here.
class facts(models.Model):
    fact_title = models.CharField(max_length=100)
    fact_fact = models.TextField()
    fact_consideration = models.TextField()
    fact_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.fact_title

class posts(models.Model):
    post_title = models.CharField(max_length=200)
    post_problem = models.CharField(max_length=200)
    post_image = models.ImageField(upload_to='images/')
    post_description = models.TextField()
    post_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.post_title
    
class logginedUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    user_query = models.TextField()
    user_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user)