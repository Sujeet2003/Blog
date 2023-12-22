from django.forms import ModelForm
from .models import facts, posts, logginedUser

class updateFact(ModelForm):
    class Meta:
        model = facts
        fields = '__all__'

class updatePost(ModelForm):
    class Meta:
        model = posts
        fields = '__all__'

class updateUserComments(ModelForm):
    class Meta:
        model = logginedUser
        fields = ['user_query']