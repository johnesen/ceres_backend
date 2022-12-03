from django.contrib import admin
from products.models import *


class CharacteristicInline(admin.TabularInline):
    model = Characteristic
    fields = ["id", "key", "value"]
    readonly_fields = ["id"]
    extra = 0


class ReviewsInlie(admin.TabularInline):
    model = ProductReviews
    fields = ["id", "reviewer", "text"]
    readonly_fields = ["id"]
    extra = 0


class ProductMediaInlie(admin.TabularInline):
    model = ProductMedia
    fields = ["id", "picture", "is_main"]
    readonly_fields = ["id"]
    extra = 0


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "description", "price", "currency", "catalog"]
    inlines = [CharacteristicInline, ProductMediaInlie, ReviewsInlie]


