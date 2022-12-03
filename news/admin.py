from django.contrib import admin
from .models import Articles, ArticleMedia


class ContentInline(admin.TabularInline):
    model = Articles
    fields = ("id", "title", "description")
    readonly_fields = ["id"]
    extra = 0


class ArticleMediaInline(admin.TabularInline):
    model = ArticleMedia
    fields = ["id", "picture", "video"]
    readonly_fields = ["id"]
    extra = 0


@admin.register(Articles)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ["id", "title"]
    inlines = [ContentInline, ArticleMediaInline]
