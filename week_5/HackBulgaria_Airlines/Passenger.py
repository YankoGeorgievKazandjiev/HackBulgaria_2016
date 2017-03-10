from flight_company import Flight

class Passenger:
    def __init__(self, first_name, last_name, flight: Flight, age):
        self.first_name = first_name
        self.last_name = last_name
        self.flight = flight
        self.age = age
