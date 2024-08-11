# SEI SEBPT220 Project 4: Fiction Fables

Tiny Fables is a blog application enabling user to share their stories with others.

<img width="1385" alt="Screenshot 2024-08-10 at 7 57 39 PM" src="https://github.com/user-attachments/assets/aad475f7-7166-4efa-a6cc-d40ebfec900d">


## How It Works

Registered users can write and post blogs. They can also edit or delete their blogs, or choose to read comments left by readers.

## Event-Flow-Frontendx

Django Web App. created with Python, Django and SQL.

## Links

- https://www.blogger.com/
- https://flashfictionmagazine.com/blog/2024/08/06/a-minor-prophet/

## Features

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




