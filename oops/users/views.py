from django.shortcuts import render
from .models import VehicleFactory

def show_vehicles(request):
    # Created vehicles 
    car = VehicleFactory.create_vehicle("car", "Toyota", 180)
    bike = VehicleFactory.create_vehicle("bike", "Yamaha", 120)

    vehicles_info = [car.vehicle_type(), bike.vehicle_type()]

    return render(request, 'vehicles/show_vehicles.html', {'vehicles_info': vehicles_info})
