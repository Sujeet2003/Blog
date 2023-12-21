from django.forms import ModelForm
from .models import facts, posts

class updateFact(ModelForm):
    class Meta:
        model = facts
        fields = '__all__'

class updatePost(ModelForm):
    class Meta:
        model = posts
        fields = '__all__'