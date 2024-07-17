from django.shortcuts import render,redirect
from .models import Vehicle
from .forms import VehicleForm

# Create your views here.

def add_vehicle(request):
    if request.method == "POST":
        form = VehicleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("vehicle_list")
    else:
        form = VehicleForm()
    
    return render(request,'add_vehicle.html',{'form':form})

def vehicle_list(request):
    vehicles = Vehicle.objects.all()
    return render(request,'vehicle_list.html',{'vehicles':vehicles})



