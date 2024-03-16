from rest_framework import serializers

from order.models import Cart, ShippingAddress


class CartSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cart
        fields = ("user", "product", "count")


class ShippingAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShippingAddress
        fields = (
            "full_name",
            "address",
            "landmark",
            "city",
            "pincode",
            "contact_number",
        )
