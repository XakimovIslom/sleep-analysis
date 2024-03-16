from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Intro(BaseModel):
    title = models.CharField(max_length=256)
    image = models.ImageField(upload_to="intro/")


class Notification(BaseModel):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="notifications"
    )
    title = models.CharField(max_length=256)
    content = models.TextField()
    is_read = models.BooleanField(default=False)
