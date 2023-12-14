from django.forms import ModelForm
from .models import facts

class updateFact(ModelForm):
    class Meta:
        model = facts
        fields = '__all__'