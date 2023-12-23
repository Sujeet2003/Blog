from django.forms import ModelForm, forms
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

class uploadPosts(ModelForm):
    class Meta:
        model = posts
        fields = ['post_title', 'post_problem', 'post_image', 'post_description']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['post_image'].required = False