from django.contrib import admin
from .models import UerProfile
# Register your models here.
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ("user","birth","phone")
    list_filter = ("phone","user",)
admin.site.register(UerProfile,UserProfileAdmin)
