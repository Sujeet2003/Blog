from django.db import models

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
    post_image = models.ImageField(upload_to='images/', blank=True, null=True)
    post_description = models.TextField()
    post_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.post_title