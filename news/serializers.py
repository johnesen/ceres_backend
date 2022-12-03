from rest_framework import serializers
from .models import Articles


class ContentSerializer(serializers.Serializer):
    id = serializers.PrimaryKeyRelatedField(read_only=True)
    title = serializers.CharField(max_length=150)
    description = serializers.CharField(max_length=5000)


class RubricSerializer(serializers.Serializer):
    id = serializers.PrimaryKeyRelatedField(read_only=True)
    title = serializers.CharField(max_length=150)

class ArticleSerializer(serializers.Serializer):
    id = serializers.PrimaryKeyRelatedField(read_only=True)
    title = serializers.CharField(max_length=150)
    description = serializers.CharField(max_length=5000)
    parent = ContentSerializer()
    contents = ContentSerializer(many=True)
    rubric = serializers.CharField(read_only=True)
