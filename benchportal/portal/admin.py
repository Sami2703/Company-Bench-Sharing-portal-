from django.contrib import admin
from .models import User, ResourceType, Resource, Booking, BookingLog

admin.site.register(User)
admin.site.register(ResourceType)
admin.site.register(Resource)
admin.site.register(Booking)
admin.site.register(BookingLog)

