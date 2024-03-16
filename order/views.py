from rest_framework import generics, permissions

from order.models import Cart, ShippingAddress
from order.permissions import IsOwnerOrReadOnly
from order.serializers import CartSerializer, ShippingAddressSerializer


class CartListCreateAPIView(generics.ListCreateAPIView):
    # queryset = Cart.objects.all()
    serializer_class = CartSerializer
    # permission_classes = (IsOwnerOrReadOnly, permissions.IsAuthenticated)

    def get_queryset(self):
        user = self.request.user
        return Cart.objects.filter(user=user)


class CartRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = (IsOwnerOrReadOnly,)


class ShippingAddressListCreateAPIView(generics.ListCreateAPIView):
    queryset = ShippingAddress.objects.all()
    serializer_class = ShippingAddressSerializer
    permission_classes = (IsOwnerOrReadOnly, permissions.IsAuthenticated)


class ShippingAddressRetrieveUpdateDestroyAPIView(
    generics.RetrieveUpdateDestroyAPIView
):
    queryset = ShippingAddress.objects.all()
    serializer_class = ShippingAddressSerializer
    permission_classes = (IsOwnerOrReadOnly,)
