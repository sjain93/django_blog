from datetime import date
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from blog.models import Article, Comment
from blog.forms import CommentForm, ArticleForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required


def root(request):
    return HttpResponseRedirect("home")

def home(request):
    context = {
        "date": date.today(),
        "article": Article.objects.filter(draft=False).order_by("-published_date"),
    }
    response = render(request, "index.html", context)
    return HttpResponse(response)


def blog_post(request, id):
    item = Article.objects.get(pk=int(id))
    art_comments = item.comments.all()
    context = {
        "blog_post": item,
        "blog_com": art_comments,
        "comment_form": CommentForm(initial={"article": id}),
    }
    response = render(request, "blog_post.html", context)
    return HttpResponse(response)

@login_required
def create_comment(request):
    post_data = request.POST
    form = CommentForm(post_data)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/home/{}".format(post_data["article"]))
    else:
        return HttpResponseRedirect("/home/{}".format(post_data["article"]))

@login_required
def create_post(request):
    if request.method == "POST":
        post_data = request.POST
        print(post_data)
        form = ArticleForm(post_data)
        if form.is_valid():
            form.user = request.user
            new_post = form.save()
            return HttpResponseRedirect(reverse(blog_post, args=[new_post.pk]))
        else:
            return HttpResponseRedirect("/home")
    else:
        form = ArticleForm()
        context = {"form": form}
        response = render(request, "new_post.html", context)
        return HttpResponse(response)


def login_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/home')
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            pw = form.cleaned_data["password"]
            user = authenticate(username=username, password=pw)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect("/home")
    else:
        form = LoginForm()

    context = {"form": form}
    return HttpResponse(render(request, "login.html", context))

@login_required
def logout_view(request):
    logout(request)
    return HttpResponseRedirect("/home")
