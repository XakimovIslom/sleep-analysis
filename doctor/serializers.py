from rest_framework import serializers

from doctor.models import Booking, Doctor


class DoctorSerializer(serializers.ModelSerializer):
    syptoms = serializers.StringRelatedField(many=True)

    class Meta:
        model = Doctor
        fields = (
            "name",
            "specialization",
            "city",
            "rating",
            "patients",
            "syptoms",
        )


class BookingSerializer(serializers.ModelSerializer):
    # user = serializers.StringRelatedField(source="user.username")
    # doctor = serializers.StringRelatedField(source="doctor.name")

    class Meta:
        model = Booking
        fields = (
            "user",
            "doctor",
            "start_time",
            "end_time",
        )
