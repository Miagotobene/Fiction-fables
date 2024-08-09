from django.db import models

# Author model here
class Author(models.Model):
    name = models.CharField(max_length=100)
    nationality = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    photo_url = models.TextField()


    def __str__(self):
        return self.name


# Create blogs model here
class Blog(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='blogs')
    title = models.CharField(max_length=100)
    slug  = models.SlugField()
    intro = models.TextField()
    content = models.TextField()
    cover_url = models.TextField()
    created_on = models.DateTimeField(auto_now_add= True)
    updated_on = models.DateTimeField(auto_now= True)

    class Meta:
        ordering = ('-created_on',)


    def __str__(self):
        return self.title


# Create comments model here
class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    username = models.CharField(max_length=100, default='Please add your name')
    content = models.CharField(max_length=300, default  ='add comments here')

    def __str__(self):
        return self.username
    
