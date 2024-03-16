from rest_framework import serializers

from common.models import Intro, Notification


class IntroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Intro
        fields = "__all__"


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = "__all__"
