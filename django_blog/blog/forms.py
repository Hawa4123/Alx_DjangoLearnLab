from django import forms
from .models import Post
from django.contrib.auth.models import User
from .models import Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Post title', 'class': 'form-control'}),
            'content': forms.Textarea(attrs={'placeholder': 'Write your post here...', 'class': 'form-control', 'rows': 10}),
        }
        class CommentForm(forms.ModelForm):
    content = forms.CharField(
        widget=forms.Textarea(
            attrs={'rows': 3, 'placeholder': 'Add a comment...'}
        ),
        label='',
        max_length=1000  # optional: limit comment length
    )

    class Meta:
        model = Comment  # links form to Comment model
        fields = ['content']  # only allow editing of content
