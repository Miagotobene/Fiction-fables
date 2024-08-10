# blog/forms.py
from django import forms
from .models import Blog, Comment, Author, Category

class AuthorForm(forms.ModelForm):

    class Meta:
        model = Author
        fields = ('name', 'nationality', 'genre', 'photo_url',)


choices = Category.objects.all().values_list('title', 'title')

choice_list = []

for item in choices:
    choice_list.append(item)


class BlogForm(forms.ModelForm):

    class Meta:
        model = Blog
        fields = ('author', 'category', 'title', 'slug', 'intro', 'content','cover_url', 'status',)

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(choices = choice_list, attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
        }



class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('username', 'content',)