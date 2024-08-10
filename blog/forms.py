# blog/forms.py
from django import forms
from .models import Blog, Comment, Author

class AuthorForm(forms.ModelForm):

    class Meta:
        model = Author
        fields = ('name', 'nationality', 'genre', 'photo_url',)

class BlogForm(forms.ModelForm):

    class Meta:
        model = Blog
        fields = ('author', 'category', 'title', 'slug', 'intro', 'content','cover_url', 'status',)

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('username', 'content',)