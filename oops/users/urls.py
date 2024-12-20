from django.urls import path
from .views import show_vehicles

urlpatterns = [
    path('', show_vehicles, name='show_vehicles'),
]
