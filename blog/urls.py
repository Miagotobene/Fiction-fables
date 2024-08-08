from django.urls import path
from . import views

urlpatterns = [
    # blog paths
    path('', views.blog_list, name='blog_list'),
    path('blogs/<int:pk>', views.blog_detail, name='blog_detail'),
    path('blogs/new', views.blog_create, name='blog_create'),


    # paths for authors
    path('/authors', views.author_list, name='author_list'),

    # paths for comments
    path('comments/', views.comment_list, name='comment_list'),
    path('comments/<int:pk>', views.comment_detail, name='comment_detail'),
    path('comments/new', views.comment_create, name='comment_create'),
]