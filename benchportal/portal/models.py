from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    USER_TYPE_CHOICES = (
        ('Admin', 'Admin'),
        ('Company', 'Company'),
    )
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES)
    company_name = models.CharField(max_length=100, null=True, blank=True)

class ResourceType(models.Model):
    name = models.CharField(max_length=50, unique=True)

class Resource(models.Model):
    RESOURCE_STATUS_CHOICES = (
        ('Available', 'Available'),
        ('Booked', 'Booked'),
    )
    name = models.CharField(max_length=100)
    resource_type = models.ForeignKey(ResourceType, on_delete=models.CASCADE)
    description = models.TextField()
    available_from = models.DateField()
    status = models.CharField(max_length=10, choices=RESOURCE_STATUS_CHOICES, default='Available')
    booked_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='booked_resources')
    booked_date = models.DateField(null=True, blank=True)

class Booking(models.Model):
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    booked_date = models.DateField(auto_now_add=True)
    released_date = models.DateField(null=True, blank=True)

class BookingLog(models.Model):
    ACTION_CHOICES = (
        ('Booked', 'Booked'),
        ('Released', 'Released'),
    )
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    action = models.CharField(max_length=10, choices=ACTION_CHOICES)
    action_date = models.DateField(auto_now_add=True)

