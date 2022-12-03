from django.contrib import admin
from catalogs.models import Catalog


class SubCatalogInline(admin.TabularInline):
    model = Catalog
    fields = ("id", "title")
    readonly_fields = ["id"]
    extra = 0


@admin.register(Catalog)
class CatlogAdmin(admin.ModelAdmin):
    list_display = ["id", "title"]
    fields = ["id", "title", "is_deleted"]
    readonly_fields = ["id"]
    inlines = [SubCatalogInline]
