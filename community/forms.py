from django import forms
from . models import Community,Comment

class CommunityForm(forms.ModelForm):
    class Meta:
        model = Community
        fields = ('title', 'movie_title','rank','content',)