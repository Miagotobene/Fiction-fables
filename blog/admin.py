from django.contrib import admin
from .models import Blog
from .models import Comment
from .models import Author
from .models import Category

#  Add search functionality for categories
class CommentItemInline(admin.TabularInline):
    model = Comment
    raw_id_fields = ['blog']


# Add search functionality for blogs
class PostAdmin(admin.ModelAdmin):
    search_fields = ['title', 'intro', 'content']
    list_display = ['title', 'slug', 'category', 'created_on', 'status']
    list_filter = ['category', 'created_on']
    inlines = [CommentItemInline]
    prepopulated_fields = {'slug': ('title', )}



#  Add search functionality for categories
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_display = ['title']
    prepopulated_fields = {'slug': ('title', )}

#  Add search functionality for categories
class CommentAdmin(admin.ModelAdmin):
    list_display = ['username', 'blog']

# Register your models here.
admin.site.register(Blog, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Author)
admin.site.register(Category, CategoryAdmin)





