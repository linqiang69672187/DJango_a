from django.urls import path
from . import views,list_views
app_name='article'
urlpatterns=[
    path('article_column/',views.article_column,name='article_column'),
    path('rename_column/',views.rename_article_column,name='rename_column'),
    path('del_column/', views.del_article_column, name='del_column'),
    path('article_post/', views.article_post, name='article_post'),
    path('article_list/', views.article_list, name='article_list'),
    path('article_detail/<int:id>/', views.article_detail, name="arcticle_detail"),
    path('del_article/', views.del_article, name="del_article"),
    path('redit_article/<int:article_id>/', views.edit_article, name="redit_article"),
    path('list_article/',list_views.article_titles,name="list_article"),
    path('list_detail/<int:id>/', list_views.article_detail, name="list_detail"),
    path('list_article_author/<str:username>/', list_views.article_titles_author, name="author_articles"),
]