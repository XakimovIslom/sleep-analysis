from django.contrib import admin
from order.models import Cart, ShippingAddress


admin.site.register(Cart)
admin.site.register(ShippingAddress)
