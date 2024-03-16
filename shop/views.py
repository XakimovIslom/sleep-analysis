from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, generics

from shop.models import Product
from shop.serializers import ProductDetailSerializer, ProductListSerializer


class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filterset_fields = ("tag", "rating")
    search_fields = ("title",)


class ProductRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer



