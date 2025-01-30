from django.contrib import admin
from .models import Vehicle, VehicleRequest, VehicleRequestHistory

@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ('make', 'model', 'registration_number', 'owner')
    search_fields = ('registration_number',)

@admin.register(VehicleRequest)
class VehicleRequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'vehicle', 'status', 'created_at')
    list_filter = ('status', 'vehicle')
    raw_id_fields = ('user', 'vehicle')

@admin.register(VehicleRequestHistory)
class VehicleRequestHistoryAdmin(admin.ModelAdmin):
    list_display = ('vehicle_request', 'changed_by', 'previous_status', 'new_status', 'change_date')
    list_filter = ('new_status',)