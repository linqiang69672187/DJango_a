from django.urls import path
from . import views

urlpatterns=[
    path('article_column/',views.article_column,name='article_column'),
    path('rename_column/',views.rename_article_column,name='rename_column'),
    path('del_column/', views.del_article_column, name='del_column'),
    path('article_post/', views.article_post, name='article_post'),
]