from django import forms
from .models import Post


class WriteForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['hash_tag', 'content']
        labels = {
            'hash_tag': 'hash_tag',
            'content': 'content',
        }
