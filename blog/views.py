from datetime import date
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from blog.models import Article

def root(request):
    return HttpResponseRedirect('home')

def home(request):
    context = {'date': date.today(), 'article': Article.objects.filter(draft=False).order_by('-published_date')}
    response = render(request, 'index.html', context)
    return HttpResponse(response)

def blog_post(request, id):
    item = Article.objects.get(pk=int(id))
    context = {'blog_post': item}
    response = render(request, 'blog_post.html', context)
    return HttpResponse(response)
