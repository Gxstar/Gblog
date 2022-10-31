'''
后台模型注册页面
'''
from django.contrib import admin
from .models import Category, Article, Comments, Tag
# Register your models here.


class ArticleAdmin(admin.ModelAdmin):
    """
    文章模型管理
    """
    list_display = ('title', 'createTime', 'updateTime')


class CommentsAdmin(admin.ModelAdmin):
    """
    文章模型管理
    """
    list_display = ('body', 'article', 'author', 'createTime')


admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Comments, CommentsAdmin)
