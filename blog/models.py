from django.db import models
from datetime import date
from django.core.validators import MinLengthValidator
from django.core.exceptions import ValidationError
from datetime import date, datetime
from django.contrib.auth.models import User

min_len = MinLengthValidator(limit_value=2)


class Article(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField(validators=[min_len])
    draft = models.BooleanField()
    published_date = models.DateField()
    author = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="poster", default=1)

    def clean(self):
        if self.draft and self.published_date < date.today():
            raise ValidationError(
                "Article must be published in the future as it is a draft"
            )

    def __str__(self):
        return self.title


class Comment(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    message = models.TextField()
    article = models.ForeignKey(
        Article, on_delete=models.CASCADE, related_name="comments"
    )

    def __str__(self):
        return self.name
