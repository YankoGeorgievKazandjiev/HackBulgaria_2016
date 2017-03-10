from Passenger import Passenger
from flight_company import Flight


class Reservation:
    def __init__(self, flight: Flight, passenger: Passenger, accepted):
        self.flight = flight
        self.passenger = passenger
        self.accepted = accepted
