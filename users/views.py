from rest_framework import generics

from users.models import User
from users.serializers import UserSerializer


class UserMeAPIView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user
