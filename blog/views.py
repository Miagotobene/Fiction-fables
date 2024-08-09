from django.shortcuts import render, redirect
from .models import Blog, Comment, Author
from .forms import BlogForm, CommentForm

# home page
def home_page(request):
    # render all blogs in the home page
    blogs = Blog.objects.all()
    return render(request, 'blog/home.html', {'blogs': blogs})


# about page
def about_page(request):
    return render(request, 'blog/about.html')

# Create views for Blogs here
# Get: get all blogs
def blog_list(request):
    blogs = Blog.objects.all()
    return render(request, 'blog/blog_list.html', {'blogs': blogs})

# Get: get a blog
def blog_detail(request, pk):
    blog = Blog.objects.get(id=pk)
    return render(request, 'blog/blog_detail.html', {'blog': blog})

# Post: create a blog
def blog_create(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            blog = form.save()
            return redirect('blog_detail', pk=blog.pk)
    else:
        form = BlogForm()
    return render(request, 'blog/blog_form.html', {'form': form})






# Create views for Authors here
def author_list(request):
    authors = Author.objects.all()
    return render(request, 'blog/author_list.html', {'authors': authors})




# Create views for Comments here
# Get: get all comments
def comment_list(request):
    comments = Comment.objects.all()
    return render(request, 'blog/comment_list.html', {'comments': comments})

# Get: get a comment
def comment_detail(request, pk):
    comment = Comment.objects.get(id=pk)
    return render(request, 'blog/comment_detail.html', {'comment': comment})

    
# Get: create a comment
def comment_create(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save()
            return redirect('comment_detail', pk=comment.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/comment_form.html', {'form': form})