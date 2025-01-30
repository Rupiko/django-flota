from django.db import models
from django.conf import settings
from django.utils import timezone

STATUS_CHOICES = (
    ('O', 'Oczekuje'),
    ('Z', 'Zatwierdzony'),
    ('R', 'Odrzucony'),
    ('W', 'W trakcie'),
    ('X', 'Zakończony'),
)

class Vehicle(models.Model):
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    registration_number = models.CharField(max_length=50, unique=True)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name="owned_vehicles"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    last_status = models.CharField(max_length=1, choices=STATUS_CHOICES, blank=True, null=True)
    last_status_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="updated_vehicles"
    )
    last_status_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.make} {self.model} ({self.registration_number})"

class VehicleRequest(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='vehicle_requests')
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name='requests')
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='O')
    created_at = models.DateTimeField(auto_now_add=True)
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(null=True, blank=True)
    purpose = models.TextField(blank=True)

    def __str__(self):
        return f"Request #{self.id} by {self.user}"

class VehicleRequestHistory(models.Model):
    vehicle_request = models.ForeignKey(VehicleRequest, on_delete=models.CASCADE, related_name='history')
    changed_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    previous_status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    new_status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    change_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"History #{self.id} for Request {self.vehicle_request.id}"