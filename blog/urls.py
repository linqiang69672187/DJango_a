from django.conf.urls import url
from django.urls import path,include
from . import views

urlpatterns=[
   # url(r'^$',views.blog_title,name="blog_title")
  #url(r'(?P<article_id>\d)/$’, views. blog_article, name=” blog_detail”),
    path(r'', views.blog_title),
    path('<int:acticle_id>/',views.blog_acticle ),
]