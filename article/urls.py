from django.urls import path
from . import views

urlpatterns=[
    path('article_column/',views.article_column,name='article_column')
]