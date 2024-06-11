from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('resource_by_type/<int:resource_type_id>/', views.resource_by_type, name='resource_by_type'),
    path('book_resource/<int:resource_id>/', views.book_resource, name='book_resource'),
    path('my_bookings/', views.my_bookings, name='my_bookings'),
    path('release_resource/<int:booking_id>/', views.release_resource, name='release_resource'),
    path('booking_log/', views.booking_log, name='booking_log')
]

