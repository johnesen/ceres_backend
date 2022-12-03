from django.contrib import admin
from django.contrib.auth.models import Group
from .models import User
from products.models import CartItem, Cart, Order


@admin.register(User)
class UserAdminv(admin.ModelAdmin):
    model = User
    list_display = ("email", "full_name", "is_active", "is_deleted")
    list_display_links = ("email", "full_name", "is_deleted")
    list_filter = ("is_active", "is_deleted", "created_at", "updated_at")
    list_editable = ("is_active",)
    readonly_fields = ("is_deleted", "created_at", "updated_at")
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "email",
                    "full_name",
                    "is_active",
                    "is_deleted",
                    "created_at",
                    "updated_at",
                )
            },
        ),
    )


admin.site.unregister(Group)
admin.site.register(CartItem)
admin.site.register(Cart)
admin.site.register(Order)
