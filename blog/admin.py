# coding: utf-8
from django.contrib import admin
from models import Article, Tag, UserLikes


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'publish', 'add_date', 'slug', 'likes', 'dislikes')
    prepopulated_fields = {"slug": ("title",)}


class TagAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    prepopulated_fields = {"slug": ("title",)}

class UserLikesAdmin(admin.ModelAdmin):
    list_display = ('user', 'article', 'like', 'dislike')

admin.site.register(Article, ArticleAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(UserLikes, UserLikesAdmin)

