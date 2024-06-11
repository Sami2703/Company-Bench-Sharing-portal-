from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import ResourceType, Resource, Booking, BookingLog

@login_required
def dashboard(request):
    resource_types = ResourceType.objects.all()
    resources_summary = {
        resource_type.name: Resource.objects.filter(resource_type=resource_type, status='Available').count()
        for resource_type in resource_types
    }
    return render(request, 'templates/dashboard.html', {'resources_summary': resources_summary})

@login_required
def resource_by_type(request, resource_type_id):
    resources = Resource.objects.filter(resource_type_id=resource_type_id, status='Available')
    return render(request, 'templates/resource_by_type.html', {'resources': resources})

@login_required
def book_resource(request, resource_id):
    resource = Resource.objects.get(id=resource_id)
    resource.status = 'Booked'
    resource.booked_by = request.user
    resource.booked_date = timezone.now()
    resource.save()
    Booking.objects.create(resource=resource, user=request.user)
    BookingLog.objects.create(resource=resource, user=request.user, action='Booked')
    return redirect('dashboard')

@login_required
def my_bookings(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'templates/my_bookings.html', {'bookings': bookings})

@login_required
def release_resource(request, booking_id):
    booking = Booking.objects.get(id=booking_id)
    booking.released_date = timezone.now()
    booking.save()
    resource = booking.resource
    resource.status = 'Available'
    resource.booked_by = None
    resource.booked_date = None
    resource.save()
    BookingLog.objects.create(resource=resource, user=request.user, action='Released')
    return redirect('my_bookings')

@login_required
def booking_log(request):
    logs = BookingLog.objects.filter(user=request.user)
    return render(request, 'templates/booking_log.html', {'logs': logs})
