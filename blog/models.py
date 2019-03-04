from django.db import models
from datetime import date

class Article(models.Model):
    title = models.CharField(max_length = 255)
    body = models.TextField()
    draft = models.BooleanField()
    published_date = models.DateField(auto_now_add=True)
    author = models.CharField(max_length = 255)

    def __str__(self):
        return self.title
