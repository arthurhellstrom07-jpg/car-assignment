# Import from modules
from modules import json_handler, classes

# Main function
def main():
    # User input for persons, the person object will then get appended to the "persons.json" file to be used later
    if input("Would you like to add a person to the list? (y/n) ").lower() == "y":
        person = classes.Person(input("Name: "), int(input("Age: ")), input("ID: "))
        if person.__dict__ in json_handler.read("data/persons.json"):
            print("This person is already in the list.")
        elif person.__dict__["id"] in [p["id"] for p in json_handler.read("data/persons.json")]:
            print("A person with this ID is already in the list.")
        else:
            json_handler.append_to_json("data/persons.json", person.__dict__)
            print("Person added to the list.")
    
    # User input for cars, the person object will then get appended to the "cars.json" file to be used later
    if input("Would you like to add a car to the list? (y/n) ").lower() == "y":
        car = classes.Car(input("Brand: "), input("Model: "), input("License Plate: "), input("Owner ID: "))
        if car.__dict__ in json_handler.read("data/cars.json"):
            print("This car is already in the list.")
        elif car.__dict__["license_plate"] in [c["license_plate"] for c in json_handler.read("data/cars.json")]:
            print("A car with this license plate is already in the list.")
        else:
            json_handler.append_to_json("data/cars.json", car.__dict__)
            print("Car added to the list.")
    
    # User input for speed cameras, the person object will then get appended to the "speed_cameras.json" file to be used later
    if input("Would you like to add a speed camera? (y/n) ").lower() == "y":
        speed_camera = classes.SpeedCamera(input("Location: "), int(input("Speed Limit: ")))
        if speed_camera.__dict__ in json_handler.read("data/speed_cameras.json"):
            print("This speed camera is already in the list.")
        else:
            json_handler.append_to_json("data/speed_cameras.json", speed_camera.__dict__)
            print("Speed camera added to the list.")

    # Variables for fine
    location = input("Enter the location of the car: ")
    speed = int(input("Enter the speed of the car: "))
    license_plate = input("Enter the license plate of the car: ")
    driver = input("Enter the name of the driver: ")
    speed_cameras = json_handler.read("data/speed_cameras.json")
    persons = json_handler.read("data/persons.json")
    cars = json_handler.read("data/cars.json")

    # Create a finecalculator object and calculate the fine, append it to "fines.json"
    fine_calculator = classes.FineCalculator(location, speed, license_plate, driver)
    fine_calculator.calculate_fine(speed_cameras, persons, cars)

    # Print all fines (Optional)
    if input("Would you like to see all fines? (y/n) ").lower() == "y":
        fines = json_handler.read("data/fines.json")
        for fine in fines:
            print(fine)
            
main()