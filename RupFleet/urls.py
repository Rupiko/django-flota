from django.contrib import admin
from django.urls import path, include
from vehicles import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', views.register_view, name='register'),
    path('', views.home_view, name='home'),
    path('vehicles/', include('vehicles.urls')),
]