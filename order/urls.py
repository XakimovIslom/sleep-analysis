from django.urls import path

from order import views

urlpatterns = [
    path("cart/", views.CartListCreateAPIView.as_view()),
    path("cart/<int:pk>/", views.CartRetrieveUpdateDestroyAPIView.as_view()),
]
