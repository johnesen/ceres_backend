from rest_framework import status, generics
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

from products.serializers import *
from products.models import *
from common.schemas.others import *


class ProductListAPIView(generics.ListAPIView):
    schema = ProductListSchema()
    queryset = Product.objects.filter(is_deleted=False).order_by("-created_at")
    permission_classes = (AllowAny,)
    serializer_class = ProductSerializer
    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter,
        DjangoFilterBackend,
    ]
    search_fields = ["title", "description", "characteristics__value"]
    ordering_fields = ["price", "created_at", "title"]
    filterset_fields = ["catalog__id"]


class CartItemAPIView(generics.CreateAPIView):
    schema = CartItemSchema()
    permission_classes = (AllowAny, )
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer


class CartAPIView(generics.ListCreateAPIView):
    schema = CartSchema()
    permission_classes = (AllowAny, )
    queryset = Cart.objects.all()
    serializer_class = CartSerializer