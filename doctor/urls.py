from django.urls import path
from doctor import views

urlpatterns = [
    # path("", views.DoctorListAPIView.as_view()),
    path("booking/", views.BookingListAPIView.as_view()),
]
