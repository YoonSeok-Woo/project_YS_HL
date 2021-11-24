from django import forms
from django.forms.widgets import Textarea
from . models import Community,Comment

class CommunityForm(forms.ModelForm):
    class Meta:
        model = Community
        fields = ('title','content','image')

class CommentForm(forms.ModelForm):
    content = forms.CharField(
        label = "새 댓글",
        widget = forms.Textarea(
            attrs={
                'class': 'col-auto',
                'placeholder': '댓글을 입력해주세요',
                'rows': '1',
            }
        )
    )
    class Meta:
        model = Comment
        exclude = ('community','user')