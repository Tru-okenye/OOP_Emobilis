from django.db import models
from abc import ABC, abstractmethod  

# abstraction
class Vehicle(ABC):
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

    @abstractmethod
    def vehicle_type(self):
        pass  

# Inheritance
class Car(Vehicle):
    def vehicle_type(self):
        return f"{self.name} is a Car, and it can go up to {self.speed} km/h."

class Bike(Vehicle):
    def vehicle_type(self):
        return f"{self.name} is a Bike, and it can go up to {self.speed} km/h."

# Polymorphism
class VehicleFactory:
    @staticmethod
    def create_vehicle(vehicle_type, name, speed):
        if vehicle_type == "car":
            return Car(name, speed)
        elif vehicle_type == "bike":
            return Bike(name, speed)
        else:
            return None
