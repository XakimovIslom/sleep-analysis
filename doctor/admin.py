from django.contrib import admin

from doctor.models import Booking, Doctor, Syptoms


admin.site.register(Doctor)
admin.site.register(Syptoms)
admin.site.register(Booking)
