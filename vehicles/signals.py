from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import VehicleRequest, VehicleRequestHistory

@receiver(pre_save, sender=VehicleRequest)
def create_history_record(sender, instance, **kwargs):
    if instance.pk:
        original = VehicleRequest.objects.get(pk=instance.pk)
        if original.status != instance.status:
            VehicleRequestHistory.objects.create(
                vehicle_request=instance,
                changed_by=instance.vehicle.owner,
                previous_status=original.status,
                new_status=instance.status
            )