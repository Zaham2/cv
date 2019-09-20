from django.db import models


# Create your models here.
class Blog(models.Model):
    title = models.TextField()
    pubDate = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/blog')

    # Shows Blog.title on admin screen
    def __str__(self):
        return self.title

    def otherMethod(self):
        # method to fix datetime
        # method to show summary of blog text
        pass
