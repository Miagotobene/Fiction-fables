from django.urls import path
from . import views

urlpatterns = [

     # paths for search
    path('blogs/search/', views.search, name='search'),

    # blog paths
    path('blogs/<int:category_pk>/<int:pk>/', views.blog_detail, name='blog_detail'),
    path('blogs/new', views.blog_create, name='blog_create'),


    # paths for authors
    path('authors', views.author_list, name='author_list'),

    # paths for post categories
    path('blogs/<int:pk>/', views.category, name='category_detail'),

   


]