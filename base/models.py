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
    
    
class projectItems(models.Model):
    project_title = models.CharField(max_length=30)
    project_description = models.TextField()
    project_poster = models.ImageField(upload_to='images/')
    project_link = models.URLField(max_length=100, null=True, blank=True)

    def __str__(self):
        return str(self.project_title)
    
class personalDetails(models.Model):
    total_experience = models.IntegerField()
    current_location = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.BigIntegerField()
    languages = models.CharField(max_length=50)

    def __str__(self):
        return str(self.current_location)
    
class personalSkills(models.Model):
    languages = models.CharField(max_length=100)
    frameworks = models.CharField(max_length=500)
    versionControl = models.CharField(max_length=200)
    others = models.CharField(max_length=100)

    def __str__(self):
        return str(self.others)
    
class contact_form(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.BigIntegerField()
    description = models.TextField()

    def __str__(self):
        return str(self.email)
    
class reviewUs(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    testinomial = models.TextField()
    testinomial_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user)