from django.db import models
from django.utils.translation import gettext_lazy as _
from common.models import BaseModel
from products.settings import CurrencyType, OrderStatus
from django.contrib.auth import get_user_model


User = get_user_model()


class Product(BaseModel):
    title = models.CharField(
        max_length=150, blank=False, null=False, verbose_name=_("title")
    )
    description = models.TextField(
        blank=False, null=False, verbose_name=_("descriptions")
    )
    catalog = models.ForeignKey(
        "catalogs.Catalog",
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        verbose_name=_("catalog"),
        related_name="products",
    )
    price = models.DecimalField(
        blank=False,
        null=False,
        max_digits=20,
        decimal_places=2,
        verbose_name=_("price"),
    )
    currency = models.CharField(
        max_length=150,
        choices=CurrencyType.choices(),
        null=False,
        blank=False,
        default=CurrencyType.USD,
    )


class Characteristic(BaseModel):
    key = models.CharField(
        max_length=100, blank=False, null=False, verbose_name=_("key")
    )
    value = models.CharField(
        max_length=300, blank=False, null=False, verbose_name=_("value")
    )
    product = models.ForeignKey(
        Product,
        blank=False,
        null=False,
        on_delete=models.CASCADE,
        verbose_name=_("product"),
        related_name="characteristics",
    )


class ProductMedia(BaseModel):
    product = models.ForeignKey(
        Product,
        blank=False,
        null=False,
        on_delete=models.CASCADE,
        verbose_name=_("product"),
        related_name="media",
    )
    picture = models.ImageField(
        upload_to="product/%Y/%m/%d", blank=True, null=True, verbose_name=_("picture")
    )
    is_main = models.BooleanField(default=False, verbose_name=_("is main picture?"))


class ProductReviews(BaseModel):
    reviewer = models.CharField(
        max_length=100, blank=False, null=False, verbose_name=_("reviewer")
    )
    text = models.CharField(
        max_length=300, blank=False, null=False, verbose_name=_("text")
    )
    product = models.ForeignKey(
        Product,
        blank=False,
        null=False,
        on_delete=models.CASCADE,
        verbose_name=_("product"),
        related_name="reviews",
    )


class CartItem(BaseModel):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        verbose_name=_("art item"),
        related_name="cart_item",
    )
    sum_amount_price = models.DecimalField(
        blank=False,
        null=False,
        max_digits=20,
        decimal_places=2,
        verbose_name=_("sum amount price"),
    )
    quantity = models.IntegerField(verbose_name=_("item amount"))


class Cart(BaseModel):
    items = models.ManyToManyField(
        CartItem, blank=True, null=True, verbose_name=_("items"), related_name="cart"
    )
    general_price = models.DecimalField(
        blank=False,
        null=False,
        max_digits=20,
        decimal_places=2,
        verbose_name=_("general price"),
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        verbose_name=_("user"),
        related_name="carts",
    )


class Order(BaseModel):
    full_name = models.CharField(
        max_length=150, blank=False, null=False, verbose_name=_("full name")
    )
    email = models.EmailField(blank=False, null=False, verbose_name=_("email"))
    phone = models.CharField(
        max_length=13, blank=False, null=False, verbose_name=_("phone")
    )
    city = models.CharField(
        max_length=25, blank=False, null=False, verbose_name=_("city")
    )
    status = models.CharField(
        max_length=50,
        choices=OrderStatus.choices(),
        verbose_name=_("order status"),
        default=OrderStatus.ON_REVIEW,
    )
    description = models.TextField(verbose_name=_("description"))
    cart = models.ForeignKey(
        Cart,
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        verbose_name=_("cart"),
        related_name="order",
    )
