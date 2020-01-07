from django.db import models

class News(models.Model):
    Title = models.CharField(max_length=120)
    Post = models.TextField()
    date = models.DateTimeField()

    def __str__(self):
        return self.Title
