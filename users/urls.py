from django.urls import path

from users import views

urlpatterns = [
    path("me/", views.UserMeAPIView.as_view()),
]
