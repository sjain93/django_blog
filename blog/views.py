from datetime import date
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from blog.models import Article

def root(request):
    return HttpResponseRedirect('home')

def home(request):
    context = {'date': date.today(), 'article': Article.objects.filter(draft=False)}
    response = render(request, 'index.html', context)
    return HttpResponse(response)
