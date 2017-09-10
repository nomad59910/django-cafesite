from django.contrib import admin
from .models import Article


class ArticleAdmin(admin.ModelAdmin):
    list_filter = ['date']
    list_display = ('title', 'date')


admin.site.register(Article, ArticleAdmin)
