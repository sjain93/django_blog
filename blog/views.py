from datetime import date
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from blog.models import Article, Comment

def root(request):
    return HttpResponseRedirect('home')

def home(request):
    context = {'date': date.today(), 'article': Article.objects.filter(draft=False).order_by('-published_date')}
    response = render(request, 'index.html', context)
    return HttpResponse(response)

def blog_post(request, id):
    item = Article.objects.get(pk=int(id))
    art_comments = item.comments.all()
    context = {'blog_post': item, 'blog_com': art_comments }
    response = render(request, 'blog_post.html', context)
    return HttpResponse(response)

def create_comment(request):
    article = Article.objects.get(pk= request.POST['article'])
    comment = article.comments.create(name=request.POST['name'],
    message=request.POST['comment']
    )
    return HttpResponseRedirect('/home/{}'.format(article.pk))
