from django.db import models
from django.contrib.auth.models import User
from django.utils import  timezone

# Create your models here.
class ArticleColumn(models.Model):
    user = models.ForeignKey(User,related_name='article_colum',on_delete=models.CASCADE)
    column=models.CharField(max_length=200)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.column

class ArticlePost(models.Model):
    author = models.ForeignKey(User,related_name='article',on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=500)
    column = models.ForeignKey(ArticleColumn,related_name="article_colum",on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(default=timezone.now())
    updated = models.DateTimeField(auto_now=True)
    users_like = models.ManyToManyField(User,related_name="articles_like",blank=True)
    class Mata:
        ordering = ("title",)
        index_together = (('id','slug'),) #建立索引，加快文章访问速度
    def __str__(self):
        return self.title
    def save(self, *args,**kargs):
        self.slug = self.title+"H"
        super(ArticlePost,self).save(*args,**kargs)