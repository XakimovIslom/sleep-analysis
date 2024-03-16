from django.conf import settings
from django.db import models

from common.models import BaseModel


class Syptoms(BaseModel):
    title = models.CharField(max_length=128)

    def __str__(self):
        return self.title


class Doctor(BaseModel):
    name = models.CharField(max_length=128)
    specialization = models.CharField(max_length=128)
    city = models.CharField(max_length=128)
    rating = models.IntegerField()
    patients = models.IntegerField()

    syptoms = models.ManyToManyField(Syptoms)

    def __str__(self):
        return self.name


class Booking(BaseModel):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True
    )
    doctor = models.ForeignKey(
        Doctor, on_delete=models.CASCADE, related_name="appointments"
    )

    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return f"{self.start_time} - {self.end_time}"
