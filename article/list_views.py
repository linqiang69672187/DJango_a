from django.shortcuts import  render
from django.core.paginator import PageNotAnInteger,Paginator,EmptyPage
from .models import ArticleColumn,ArticlePost
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.http import HttpResponse
import redis
from django.conf import settings

r = redis.StrictRedis(host=settings.REDIS_HOST,port=settings.REDIS_PORT,db=settings.RDIS_DB)

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
    total_views = r.incr("article:{}:views".format(article.id))
    return render(request,"article/list/article_detail.html",{"article":article,"total_views":total_views})

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

@csrf_exempt
@require_POST
@login_required(login_url='/account/login/')
def like_article(request):
    article_id =request.POST.get("id")
    action = request.POST.get("action")
    if article_id and action:
        try:
            article = ArticlePost.objects.get(id=article_id)
            if action=="like":
                article.users_like.add(request.user)
                return HttpResponse("1")
            else:
                article.users_like.remove(request.user)
                return HttpResponse("2")
        except:
            return HttpResponse("none")


