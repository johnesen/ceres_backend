from rest_framework import status, generics
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

from .serializers import *
from .models import *
from common.schemas.others import *


class ArticleListAPIView(generics.ListAPIView):
    schema = ArticleListSchema()

    queryset = Articles.objects\
        .filter(is_deleted=False, parent=None)\
        .order_by("-created_at")

    permission_classes = (AllowAny,)
    serializer_class = ArticleSerializer
    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter,
        DjangoFilterBackend,
    ]
    ordering_fields = ["created_at", "title"]
    search_fields = ["title", "description", "parent__title", "contents__title"]
    filterset_fields = ["rubric"]
