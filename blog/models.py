from django.db import models

# Create blogs model here
class Blog(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    cover_url = models.TextField()

    def __str__(self):
            return self.title

# Create comments model here
class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    username = models.CharField(max_length=100, default='Please add your name')
    content = models.CharField(max_length=300, default  ='add comments here')

    def __str__(self):
        return self.username
    

