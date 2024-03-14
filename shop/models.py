from django.db import models

from common.models import BaseModel


class Tag(BaseModel):
    title = models.CharField(max_length=128)

    def __str__(self) -> str:
        return self.title


class Product(BaseModel):
    title = models.CharField(max_length=256)
    image = models.ImageField(upload_to="shop/")
    content = models.TextField()
    short_content = models.TextField()
    price = models.IntegerField()
    tag = models.ManyToManyField(Tag)
    rating = models.IntegerField()

    def __str__(self):
        return self.title
