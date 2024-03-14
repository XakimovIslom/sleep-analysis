from rest_framework import serializers

from shop.models import Product


class ProductListSerializer(serializers.ModelSerializer):
    tag = serializers.StringRelatedField(many=True)

    class Meta:
        model = Product
        fields = ("short_content", "image", "tag", "price")


class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ("image", "title", 'price', "rating", "content")
