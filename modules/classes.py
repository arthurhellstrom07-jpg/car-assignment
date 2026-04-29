from dataclasses import dataclass
from datetime import datetime

from modules import json_handler

@dataclass
class Person:
    name: str
    age: int
    id: str

@dataclass
class Car:
    brand: str
    model: str
    license_plate: str
    owner_id: str

@dataclass
class SpeedCamera:
    location: str
    speed_limit: int

@dataclass
class Fine:
    person: str
    license_plate: str
    infraction: str
    amount: int

class FineCalculator:
    def __init__(self, location: str, speed: int, license_plate: str, driver: str):
        self.location = location
        self.speed = speed
        self.license_plate = license_plate
        self.driver = driver
    
    def calculate_fine(self, speed_cameras: list[dict], persons: list[dict], cars: list[dict]):
        # Fetch data for calculating fine
        matching_speed_camera = next((s for s in speed_cameras if s.get("location") == self.location), None)
        speed_limit = matching_speed_camera["speed_limit"] if matching_speed_camera else None
        current_car = next((c for c in cars if c["license_plate"] == self.license_plate), None)
        current_person = next((p for p in persons if p["name"] == self.driver), None)

        # Create fine for speeding
        if speed_limit and self.speed > speed_limit:
            infraction = f"Speeding at {self.speed} km/h in a {speed_limit} km/h zone"
            amount = (self.speed - speed_limit) * 100
            fine = Fine(self.driver, self.license_plate, infraction, amount)
            json_handler.append_to_json("data/fines.json", fine.__dict__)
            print(fine.__dict__)

        # Create fine for underage driving
        if current_person and current_person["age"] < 18:
            infraction = "Driving underage"
            amount = 500
            fine = Fine(self.driver, self.license_plate, infraction, amount)
            json_handler.append_to_json("data/fines.json", fine.__dict__)
            print(fine.__dict__)
        
        # Create fine for driving a stolen car
        if current_car and current_person and current_car["owner_id"] != current_person["id"]:
            infraction = "Driving a stolen car"
            amount = 300
            fine = Fine(self.driver, self.license_plate, infraction, amount)
            json_handler.append_to_json("data/fines.json", fine.__dict__)
            print(fine.__dict__)
        
        # Create fine for driving an unregistered car
        if self.license_plate not in [c["license_plate"] for c in cars]:
            infraction = "Driving a car that is not registered"
            amount = 200
            fine = Fine(self.driver, self.license_plate, infraction, amount)
            json_handler.append_to_json("data/fines.json", fine.__dict__)
            print(fine.__dict__)
        
        # Grant a driver money for good taste in cars
        if current_car and current_car["brand"] in ["Nissan", "Mitsubishi", "Mazda", "Honda", "Toyota"] and current_car["model"] in ["Skyline", "Fairlady Z", "Silvia", "Lancer Evolution", "Eclipse", "RX-7", "Miata", "Civic", "Integra", "NSX", "Corolla", "Sprinter", "Trueno", "Supra"]:
            infraction = "Good taste in cars"
            amount = -100
            fine = Fine(self.driver, self.license_plate, infraction, amount)
            json_handler.append_to_json("data/fines.json", fine.__dict__)
            print(fine.__dict__)