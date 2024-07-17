# mini/urls.py
from django.urls import path
from . import views

urlpatterns = [
	path('add-vehicle/', views.add_vehicle, name='add_vehicle'),
	path('vehicle-list/', views.vehicle_list, name='vehicle_list'),
]
