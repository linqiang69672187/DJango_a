from django.shortcuts import render,get_object_or_404
from django.shortcuts import  HttpResponse
from .models import BlogArticles
# 将请求定位到index.html文件中
def index(request):
    return render(request,'index.html')

def blog_title(request):
    blogs = BlogArticles.objects.all()
    return  render(request,"blog/titles.html",{"blogs":blogs})

def blog_acticle(request,acticle_id):
    # blog = BlogArticles.objects.get(id=acticle_id)
     blog = get_object_or_404(BlogArticles, id=acticle_id)
     publish = blog.publish
     return  render(request,"blog/content.html",{"blog":blog,"publish":publish})

# Create your views here.
