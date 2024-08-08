# blog/forms.py
from django import forms
from .models import Blog, Comment, Author

class BlogForm(forms.ModelForm):

    class Meta:
        model = Blog
        fields = ('title', 'cover_url', 'content',)

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('username', 'content',)