from django.contrib import admin
from .models import BlogArticles
# Register your models here.
class BlogActiclesAdmin(admin.ModelAdmin):
    list_display = ("tile","author","publish")
    list_filter = ("publish","author")
    search_fields = ("tile","body")
    raw_id_fields = ("author",)
    date_hierarchy = ("publish")
    ordering = ["publish","author"]

admin.site.register(BlogArticles,BlogActiclesAdmin)
