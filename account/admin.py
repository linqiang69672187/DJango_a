from django.contrib import admin
from .models import UerProfile,UserInfo
# Register your models here.
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ("user","birth","phone")
    list_filter = ("phone","user",)
admin.site.register(UerProfile,UserProfileAdmin)
class UserInfoAdmin(admin.ModelAdmin):
    list_display = ("user","school","company","profession","address","aboutme","photo")
    list_filter = ("school","company","profession")
admin.site.register(UserInfo,UserInfoAdmin)