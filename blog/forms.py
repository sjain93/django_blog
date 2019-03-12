from django.forms import ModelForm, HiddenInput, DateInput
from blog.models import Comment, Article

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        widgets = {'article': HiddenInput()}
        fields = ['name', 'message', 'article']

class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'body', 'author', 'published_date', 'draft']
        widgets = {
            'published_date': DateInput(attrs={'type': 'date'})
        }
