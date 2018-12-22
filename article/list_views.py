from django.shortcuts import  render
from django.core.paginator import PageNotAnInteger,Paginator,EmptyPage
from .models import ArticleColumn,ArticlePost
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User

def article_titles(request):
    articles_title = ArticlePost.objects.all()
    paginator = Paginator(articles_title,2)
    page = request.GET.get("page")
    try:
        current_page = paginator.page(page)
    except PageNotAnInteger:
        current_page = paginator.page(1)
    except EmptyPage:
        current_page = paginator.page(paginator.num_pages)
    articles = current_page.object_list
    return render(request,"article/list/article_titles.html",{"articles":articles,"page":current_page})

def article_detail(request,id):
    article = get_object_or_404(ArticlePost,id=id)
    return render(request,"article/list/article_detail.html",{"article":article})

def article_titles_author(request,username=None):
    if username:
        user = User.objects.get(username=username)
        arcticles= ArticlePost.objects.filter(author=user)
    else:
        arcticles = ArticlePost.objects.all()
    paginator =Paginator(arcticles,2)
    page = request.GET.get("page")
    try:
        current_page = paginator.page(page)
    except PageNotAnInteger:
        current_page = paginator.page(1)
    except EmptyPage:
        current_page = paginator.page(paginator.num_pages)
    articlespage = current_page.object_list

    return render(request,"article/list/author_articles.html",{"articles":articlespage,"page":current_page})
