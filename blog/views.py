from django.shortcuts import render
from .models import Blog, Comment, Author

# Create views for Authors here
def author_list(request):
    authors = Author.objects.all()
    return render(request, 'blog/author_list.html', {'authors': authors})

# Create views for Blogs here
def blog_list(request):
    blogs = Blog.objects.all()
    return render(request, 'blog/blog_list.html', {'blogs': blogs})



# Create views for Comments here
def comment_list(request):
    comments = Comment.objects.all()
    return render(request, 'blog/comment_list.html', {'comments': comments})