from date_class import Date
from Terminal import Terminal
import Passenger


class Flight:
    def __init__(self, start_time, end_time, max_passengers,
                 from_dest, to_dest, terminal, declined):
        self.start_time = start_time
        self.end_time = end_time
        self.max_passengers = max_passengers
        self.from_dest = from_dest
        self.to_dest = to_dest
        self.terminal = terminal
        self.declined = declined
        self.passengers = []
        self.passengers_count = len(self.passengers)
        self.reservations = []


    def decline_flight(self):
        self.declined = True

    def has_empty_seats(self):
        return self.max_passengers >self.passengers_count

    def passenger_reservations(self):
        return self.reservations

    def get_flight_duration(self):
        return self.end_time - self.start_time

    def flight_duration(self):
        return self.end_time - self.start_time

    def add_reservations(self, reservations):
        self.reservations.extend(reservations)

    def add_passengers(self, passengers):
        self.passengers.extend(passengers)
        self.passengers_count = len(self.passengers)

    def passengers_under_18(self):
        return [passenger for passenger in self.passengers if passenger.age < 18]
