from django.urls import path
from . import views

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