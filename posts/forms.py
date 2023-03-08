from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content',  'importance')


class PostUpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content')