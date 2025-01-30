# vehicles/urls.py
from django.urls import path
from . import views

app_name = 'vehicles'  # Namespace aplikacji

urlpatterns = [
    path('request/', views.request_vehicle_view, name='request_vehicle'),
    path('requests/', views.vehicle_request_list_view, name='vehicle_request_list'),  # TA ŚCIEŻKA!
    path('requests/<int:pk>/', views.vehicle_request_detail_view, name='vehicle_request_detail'),
    path('status/', views.vehicle_status_list_view, name='vehicle_status_list'),
]