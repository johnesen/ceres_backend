from rest_framework import serializers
from products.models import *
from catalogs.serializers import CatalogSerializer
from users.serializers import UserSerializer

class CharacteristicSerializer(serializers.Serializer):
    id = serializers.PrimaryKeyRelatedField(read_only=True)
    key = serializers.CharField(max_length=100, read_only=True)
    value = serializers.CharField(max_length=300, read_only=True)


class ProductMediaSerializer(serializers.Serializer):
    id = serializers.PrimaryKeyRelatedField(read_only=True)
    picture = serializers.ImageField(read_only=True)
    is_main = serializers.BooleanField(read_only=True)


class ProductReviewSerializer(serializers.Serializer):
    id = serializers.PrimaryKeyRelatedField(read_only=True)
    reviewer = serializers.CharField(max_length=100, read_only=True)
    text = serializers.CharField(max_length=300, read_only=True)
    created_at = serializers.DateTimeField(read_only=True)


class ProductSerializer(serializers.Serializer):
    id = serializers.PrimaryKeyRelatedField(read_only=True)
    title = serializers.CharField(max_length=150, read_only=True)
    description = serializers.CharField(max_length=5000, read_only=True)
    price = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)
    currency = serializers.CharField(max_length=150, read_only=True)
    catalog = CatalogSerializer(read_only=True)
    characteristics = CharacteristicSerializer(many=True, read_only=True)
    media = ProductMediaSerializer(many=True, read_only=True)
    reviews = ProductReviewSerializer(many=True, read_only=True)



# serilizers for cart, cart items and orders

class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ("id", "product", "sum_amount_price", "quantity")

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['product'] = ProductSerializer(instance.product).data
        return data


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ('id', "items", 'general_price', "user")

    def to_representation(self, instance):
        data = super().to_representation(instance)
        # data['items'] = CartItemSerializer(instance.items, many=True),data
        data['user'] = UserSerializer(instance.user).data
        return data