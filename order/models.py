from django.conf import settings
from django.db import models

from common.models import BaseModel
from shop.models import Product


class Cart(BaseModel):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="cart"
    )
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    count = models.IntegerField(default=0)

    # class Meta:
    #     unique_together = ("user", "product")

    @property
    def get_total_price(self):
        return self.count * self.product.price


class ShippingAddress(BaseModel):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True
    )
    cart = models.ForeignKey(Cart, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=200, null=False)
    landmark = models.CharField(max_length=256)
    city = models.CharField(max_length=200, null=False)
    pincode = models.CharField(max_length=200, null=False)
    shipping_fee = models.IntegerField()

    def __str__(self):
        return self.address

    @property
    def full_name(self):
        return self.user.first_name + self.user.last_name

    @property
    def contact_number(self):
        return self.user.phone_number

    @property
    def get_total_price_with_fee(self):
        return self.shipping_fee + self.cart.get_total_price
