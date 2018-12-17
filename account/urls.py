from django.conf.urls import url
from django.urls import path,include
from . import views
app_name='account'
#2.0开始namespace设置app_name
urlpatterns=[
   # url(r'^$',views.blog_title,name="blog_title")
  #url(r'(?P<article_id>\d)/$’, views. blog_article, name=” blog_detail”),
    path(r'login/', views.user_login,name='user_login'),
]