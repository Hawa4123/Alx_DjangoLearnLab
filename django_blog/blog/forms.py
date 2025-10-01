from django import forms
from .models import Post, Comment
from taggit.forms import TagWidget  # ✅ Import TagWidget for tags


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']  # ✅ include tags
        widgets = {
            'tags': TagWidget(),  # ✅ Tag input widget
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
