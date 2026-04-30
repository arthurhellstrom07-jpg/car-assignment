from dataclasses import dataclass   # Dataclass doesn't require the __init__ dunder function of normal classes, which makes for cleaner code

from modules import json_handler    # Import the json handler module for effective code i guess

# Class for person
@dataclass
class Person:
    name: str
    age: int
    id: str

# Class for car
@dataclass
class Car:
    brand: str
    model: str
    license_plate: str
    owner_id: str

# Class for speed camera
@dataclass
class SpeedCamera:
    location: str
    speed_limit: int

# Class for fine
@dataclass
class Fine:
    person: str
    license_plate: str
    infraction: str
    amount: int

# Class for finecalculator
class FineCalculator:
    # Class constructor for the finecalculator with necessary variables
    def __init__(self, location: str, speed: int, license_plate: str, driver: str):
        self.location = location
        self.speed = speed
        self.license_plate = license_plate
        self.driver = driver
    
    # Fine calculator for all existing infractions
    def calculate_fine(self, speed_cameras: list[dict], persons: list[dict], cars: list[dict]):
        # Fetch data for calculating fine
        matching_speed_camera = next((s for s in speed_cameras if s.get("location") == self.location), None)
        speed_limit = matching_speed_camera["speed_limit"] if matching_speed_camera else None
        current_car = next((c for c in cars if c["license_plate"] == self.license_plate), None)
        current_person = next((p for p in persons if p["name"] == self.driver), None)

        # Appends new person to list if the given person isn't in the register
        if current_person == None:
            # Same code as in main
            person = Person(self.driver, int(input(f"Age of {self.driver}: ")), input("ID: "))
            if person.__dict__ in json_handler.read("data/persons.json"):
                print("This person is already in the list.")
            elif person.__dict__["id"] in [p["id"] for p in json_handler.read("data/persons.json")]:
                print("A person with this ID is already in the list.")
            else:
                json_handler.append_to_json("data/persons.json", person.__dict__)
                print("Person added to the list.")
            # Set the person that is calculated to the one just created
            current_person = person.__dict__

        # Create fine for speeding if speed limit is not None and the speed of the car is greater than the speed limit
        if speed_limit and self.speed > speed_limit:
            # Create variables to make a fine object
            infraction = f"Speeding at {self.speed} km/h in a {speed_limit} km/h zone"
            amount = (self.speed - speed_limit) * 100
            # Create a fine object
            fine = Fine(self.driver, self.license_plate, infraction, amount)
            # add the dict of the fine object to the fines json file
            json_handler.append_to_json("data/fines.json", fine.__dict__)
            # print the dict of the fine object for clarification
            print(fine.__dict__)

        # Create fine for underage driving if current person is not None and the age of the person is less than 18
        if current_person and current_person["age"] < 18:
            # Extremely similar to the previous if statement, read it for context of the workings and functionality of this if statement
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