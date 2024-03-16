from rest_framework import serializers

from common.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "phone_number",
            "height",
            "weight",
            "dob",
            "age",
        )
