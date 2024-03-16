from django.urls import path
from common import views

urlpatterns = [
    path('', views.IntroListAPIView.as_view()),
    path('notification/', views.NotificationListAPIView.as_view()),
]
