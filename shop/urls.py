from django.urls import path

from shop import views

urlpatterns = [
    path("", views.ProductListAPIView.as_view()),
    path("detail/<int:pk>/", views.ProductRetrieveAPIView.as_view()),
]
