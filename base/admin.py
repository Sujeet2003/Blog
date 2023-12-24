from django.contrib import admin
from .models import facts, posts, logginedUser, projectItems, personalDetails, personalSkills

# Register your models here.
admin.site.register(facts)
admin.site.register(posts)
admin.site.register(logginedUser)
admin.site.register(projectItems)
admin.site.register(personalDetails)
admin.site.register(personalSkills)