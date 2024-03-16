from rest_framework import generics

from common.models import Intro, Notification
from common.serializers import IntroSerializer, NotificationSerializer


class IntroListAPIView(generics.ListAPIView):
    queryset = Intro.objects.all()
    serializer_class = IntroSerializer
    pagination_class = None


class NotificationListAPIView(generics.ListAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    pagination_class = None
