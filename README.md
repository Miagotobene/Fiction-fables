# SEI SEBPT220 Project 4: Fiction Fables

Tiny Fables is a blog application enabling users to share their stories with others.

<img width="1385" alt="Screenshot 2024-08-10 at 7 57 39 PM" src="https://github.com/user-attachments/assets/aad475f7-7166-4efa-a6cc-d40ebfec900d">


## How It Works

Registered users can write and post blogs. They can also edit or delete their blogs, or choose to read comments left by readers.

## Tiny Fables-Frontend

Django Web App. created with Python, Django and SQL.

## Links

- https://www.blogger.com/
- https://flashfictionmagazine.com/blog/2024/08/06/a-minor-prophet/

## Features
- ** ERD:**
<img width="1061" alt="Screenshot 2024-08-06 at 9 55 55 PM" src="https://github.com/user-attachments/assets/c0ac9d60-db2e-498a-93fa-29106a2a74e9">

- ** Wireframe:**
![image](https://github.com/user-attachments/assets/a747e726-e607-44cf-8e8a-b8115bad5d49)


### Front End Routing

- **Routes - frontend:**

```py
urlpatterns = [

    path('/', views.home_page, name='home_page'),
     # paths for search
    path('blogs/search/', views.search, name='search'),

    # blog paths
    path('blogs/<int:pk>/', views.blog_detail, name='blog_detail'),
    path('blogs/new', views.blog_create, name='blog_create'),
    path('blogs/<int:pk>/edit/', views.blog_edit, name='blog_edit'),
    path('blogs/<int:pk>/delete/', views.blog_delete, name='blog_delete'),



    # paths for authors
    path('blogs/authors', views.author_list, name='author_list'),
    path('blogs/authors/new', views.author_create, name='author_create'),

    # paths for post categories
    path('blogs/<int:pk>/', views.category, name='category_detail'),


]

```

## Code Snippets

```py
# Create blogs model here
class Blog(models.Model):
    Active = 'active'
    Draft = 'Draft'

    # status of a post 
    STATUS = (
        (Active, 'Active'),
        (Draft, 'Draft')
    )

    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='blogs')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='blogs')
    title = models.CharField(max_length=100)
    slug  = models.SlugField()
    intro = models.TextField()
    content = models.TextField()
    cover_url = models.CharField(max_length=200)
    created_on = models.DateTimeField(auto_now_add= True)
    updated_on = models.DateTimeField(auto_now= True)
    status = models.CharField(max_length=10, choices=STATUS, default = Active)

    class Meta:
        ordering = ('-created_on',)


    def __str__(self):
        return self.title

```

```py
 Create views for Blogs here
# Get: get a blog
def blog_detail(request, pk):
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


#  Edit a blog
def blog_edit(request, pk):
    blog = Blog.objects.get(pk=pk, status=Blog.Active)
    if request.method == "POST":
        form = BlogForm(request.POST, instance=blog)
        if form.is_valid():
            blog = form.save()
            return redirect('blog_detail', pk=pk)
    else:
        form = BlogForm(instance=blog)
    return render(request, 'blog/edit_form.html', {'form': form})


# Delete a blog
def blog_delete(request, pk):
    blog = Blog.objects.get(id=pk)
    if request.method == 'POST':
        blog.delete()
        return redirect('home_page')
    return render(request, 'blog/delete_form.html', {'blog': blog})
```

## User Stories

1. **Create an account:**
   - User can create an account
2. **Post to a blog:**
   - User can post a blog
3. **Edit a blog::**
   - User can edit a blog
4. **Delete a blog::**
   - User can delete a blog
5. **Read comments on a blog:**
   - User can read comments on their blogs
6. **Add comments to a different blog:**
   - User can comment on another user's blog
7. **Search for blogs:**
   - User can search for a blog with a particular title

## Setup Instructions for Local Deployment

To set up this project locally, follow these steps:

1. **Clone the repository:**

   ```bash
   git clone
   ```

2. **Navigate to the project directory:**

   ```bash
   cd
   ```

3. **Install dependencies:**

   ```bash
   brew install pipenv
   pipenv install django
   pipenv install psycopg2-binary
   ```

4. **Activate your virtual environment :**
   pipenv shell

5. **Start project :**
   pipenv run django-admin startproject my_app.

6. **Set up the environment variables:**

   - Create a `.env` file in the root directory.
   - Add the following environment variables:
     ```
     'http://localhost:8000'
     ```
## Mockups

![Screenshot 2024-08-10 at 8 03 40 PM](https://github.com/user-attachments/assets/1cc701c3-706a-4ecc-80cb-f6ef9753480f)


<img width="609" alt="Screenshot 2024-08-10 at 7 58 33 PM" src="https://github.com/user-attachments/assets/9e678676-38d5-425d-a1e7-9d5ed863dc1e">




