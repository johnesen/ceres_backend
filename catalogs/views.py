from rest_framework import status, generics
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from catalogs.serializers import CatalogSerializer
from common.schemas.others import MainGETSchema
from catalogs.models import Catalog

class CatalogsListAPIView(generics.GenericAPIView):
    schema = MainGETSchema()
    permission_classes = (AllowAny,)
    serializer_class = CatalogSerializer
    queryset = Catalog.objects.filter(is_deleted=False, parent=None).order_by("-created_at")

    def get(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(
            data={
                "message": "List of the catalogs",
                "data": serializer.data,
                "status": "OK",
            },
            status=status.HTTP_200_OK,
        )   