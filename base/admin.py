from django.contrib import admin
from .models import facts, posts, logginedUser

# Register your models here.
admin.site.register(facts)
admin.site.register(posts)
admin.site.register(logginedUser)