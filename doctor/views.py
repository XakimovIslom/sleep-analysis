from django.db.models import Q
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


# class BookingCreateAPIView(generics.ListCreateAPIView):
#     queryset = Booking.objects.all()
#     serializer_class = BookingSerializer

#     def get_queryset(self):
#         qs = super(BookingListAPIView, self).get_queryset()
#         check_in = self.request.POST.get("check_in")
#         check_out = self.request.POST.get("check_out")
#         if check_in and check_out:
#             qs = qs.filter(
#                 ~Q(start_date__range=[check_in, check_out])
#                 or ~Q(end_date__range=[check_in, check_out])
#             )
#         return qs
