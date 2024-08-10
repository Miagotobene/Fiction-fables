from django.db import models

# Author model here
class Author(models.Model):
    name = models.CharField(max_length=100)
    nationality = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    photo_url = models.TextField()


    def __str__(self):
        return self.name
    

# Create category model here
class Category(models.Model):
    title = models.CharField(max_length=200)
    slug  = models.SlugField()
    
    class Meta:
        ordering = ('title',)

    def __str__(self):
        return self.title

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
    cover_url = models.TextField()
    created_on = models.DateTimeField(auto_now_add= True)
    updated_on = models.DateTimeField(auto_now= True)
    status = models.CharField(max_length=10, choices=STATUS, default = Active)

    class Meta:
        ordering = ('-created_on',)


    def __str__(self):
        return self.title


# Create comments model here
class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    username = models.CharField(max_length=200, default='')
    content = models.TextField()
    

    def __str__(self):
        return self.username
    
