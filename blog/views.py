from django.shortcuts import render, redirect
from django.db.models import Q
from .models import Blog, Comment, Author, Category
from .forms import BlogForm, CommentForm, AuthorForm

# home page
def home_page(request):
    # render all blogs in the home page: Get: get all blogs
    blogs = Blog.objects.filter(status = Blog.Active)
    return render(request, 'blog/home.html', {'blogs': blogs})


# about page
def about_page(request):
    return render(request, 'blog/about.html')

# sign up page
def sign_page(request):
    return render(request, 'blog/signup.html')

# Create views for Blogs here
# Get: get a blog
def blog_detail(request, category_pk, pk):
    blog = Blog.objects.get(pk=pk, status=Blog.Active)

    # Comment form code goes here
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.blog = blog
            comment.save()
            return redirect('blog_detail', pk=pk)
    else:
        form = CommentForm()
    return render(request, 'blog/blog_detail.html', {'blog': blog, 'form': form})

#  Edit a blog
def blog_edit(request, pk):
    blog = Blog.objects.get(pk=pk)
    if request.method == "POST":
        form = BlogForm(request.POST, instance=blog)
        if form.is_valid():
            blog = form.save()
            return redirect('blog_detail', pk=blog.pk)
    else:
        form = BlogForm(instance=blog)
    return render(request, 'blog/blog_form.html', {'form': form})


# Delete a blog
def blog_delete(request, pk):
    Blog.objects.get(id=pk).delete()
    return redirect('blog_detail')



# Create views for Categories here
def category(request, pk):
    category = Category.objects.get(pk=pk)
    blogs = category.blogs.filter(status=Blog.Active)

    return render(request, 'blog/category.html', {'category': category, 'blogs': blogs})


# Create views for Search here
def search(request):
    query = request.GET.get('query', '')
    blogs = Blog.objects.filter(status=Blog.Active).filter(Q(title__icontains=query) | Q(intro__icontains=query) | Q(content__icontains=query))
    return render(request, 'blog/search.html', {'blogs': blogs, 'query': query})



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
def author_create(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            blog = form.save()
            return redirect('blog_detail', pk=blog.pk)
    else:
        form = AuthorForm()
    return render(request, 'blog/author_form.html', {'form': form})







# # Create views for Comments here
# # Get: get all comments
# def comment_list(request):
#     comments = Comment.objects.all()
#     return render(request, 'blog/comment_list.html', {'comments': comments})

# # Get: get a comment
# def comment_detail(request, pk):
#     comment = Comment.objects.get(id=pk)
#     return render(request, 'blog/comment_detail.html', {'comment': comment})

    
# # Get: create a comment
# def comment_create(request):
#     if request.method == 'POST':
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             comment = form.save()
#             return redirect('comment_detail', pk=comment.pk)
#     else:
#         form = CommentForm()
#     return render(request, 'blog/comment_form.html', {'form': form})