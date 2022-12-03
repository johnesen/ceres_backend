from rest_framework import serializers

class ChildCatalogSerializer(serializers.Serializer):
    id = serializers.PrimaryKeyRelatedField(read_only=True)
    title = serializers.CharField(max_length=150, read_only=True)

class CatalogSerializer(serializers.Serializer):
    id = serializers.PrimaryKeyRelatedField(read_only=True)
    title = serializers.CharField(max_length=150, read_only=True)
    parent = ChildCatalogSerializer(read_only=True)
    children = ChildCatalogSerializer(many=True, read_only=True)
    