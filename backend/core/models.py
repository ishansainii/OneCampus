from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = 'ADMIN', 'Admin'
        CUSTOMER = 'CUSTOMER', 'Customer'
        DELIVERY = 'DELIVERY', 'Delivery Personnel'
        CANTEEN = 'CANTEEN', 'Canteen Staff'

    role = models.CharField(max_length=20, choices=Role.choices, default=Role.CUSTOMER)
    phone_number = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"


class Canteen(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='canteens')
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='canteens/', blank=True, null=True)
    location = models.CharField(max_length=255)
    rating = models.FloatField(default=0.0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Delivery(models.Model):
    class Status(models.TextChoices):
        ONLINE = 'ONLINE', 'Online'
        OFFLINE = 'OFFLINE', 'Offline'
        BUSY = 'BUSY', 'Busy'

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='delivery_profile')
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.OFFLINE)
    current_latitude = models.FloatField(blank=True, null=True)
    current_longitude = models.FloatField(blank=True, null=True)
    
    def __str__(self):
        return f"Delivery: {self.user.username}"
