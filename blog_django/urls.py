"""
URL configuration for blog_django project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from blog.views import home_page
from blog.views import about_page
from blog.views import sign_page



urlpatterns = [
    path('admin', admin.site.urls),
    path('', home_page, name='homepage'),
    path('about/', about_page, name='aboutpage'),
    path('signup/', sign_page, name='signpage'),

    path('blogs', include('blog.urls')),
]
