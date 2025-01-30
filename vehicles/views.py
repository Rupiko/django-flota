from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .models import Vehicle, VehicleRequest
from .forms import VehicleRequestForm

def home_view(request):
    return render(request, 'home.html')

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Rejestracja zakończona sukcesem! Zaloguj się.')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def request_vehicle_view(request):
    if request.method == 'POST':
        form = VehicleRequestForm(request.POST)
        if form.is_valid():
            vehicle_request = form.save(commit=False)
            vehicle_request.user = request.user
            vehicle_request.save()
            messages.success(request, 'Wniosek został złożony!')
            return redirect('vehicles:vehicle_request_list')  # Poprawiona linia!
    else:
        form = VehicleRequestForm()
    return render(request, 'vehicles/request_vehicle.html', {'form': form})

@login_required
def vehicle_request_list_view(request):
    requests = VehicleRequest.objects.filter(user=request.user)
    return render(request, 'vehicles/vehicle_request_list.html', {'requests': requests})

@login_required
def vehicle_request_detail_view(request, pk):
    req = get_object_or_404(VehicleRequest, pk=pk)
    is_owner = request.user == req.vehicle.owner
    return render(request, 'vehicles/vehicle_request_detail.html', {'req': req, 'is_owner': is_owner})

@login_required
def approve_request_view(request, pk):
    req = get_object_or_404(VehicleRequest, pk=pk)
    if request.method == 'POST' and request.user == req.vehicle.owner:
        req.status = 'Z'
        req.save()
        messages.success(request, 'Wniosek zatwierdzony!')
    else:
        messages.error(request, 'Brak uprawnień!')
    return redirect('vehicles:vehicle_request_detail', pk=pk)  # Poprawiona linia!

@login_required
def reject_request_view(request, pk):
    req = get_object_or_404(VehicleRequest, pk=pk)
    if request.method == 'POST' and request.user == req.vehicle.owner:
        req.status = 'R'
        req.save()
        messages.success(request, 'Wniosek odrzucony!')
    else:
        messages.error(request, 'Brak uprawnień!')
    return redirect('vehicles:vehicle_request_detail', pk=pk)  # Poprawiona linia!

@login_required
def vehicle_status_list_view(request):
    vehicles = Vehicle.objects.all()
    return render(request, 'vehicles/vehicle_status_list.html', {'vehicles': vehicles})