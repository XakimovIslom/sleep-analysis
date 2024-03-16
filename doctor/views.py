from rest_framework import filters, generics

from doctor.models import Booking, Doctor
from doctor.serializers import BookingSerializer, DoctorSerializer


class DoctorListAPIView(generics.ListAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = (
        "name",
        "syptoms__title",
    )


class BookingListAPIView(generics.ListAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    def get_object(self):
        return super().get_object(user=self.request.user)
