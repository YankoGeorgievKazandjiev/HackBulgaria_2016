from Duration import Duration
from Passenger import Passenger
from Terminal import Terminal
from Reservation import Reservation
from flight_company import Flight
from date_class import Date

class Airline:
    def __init__(self, flights):
        self.flights = [flight for flight in flights if not flight.declined]

    def declined_flight(self, flight):
        flight.declined_flight()
        self.flights.remove(flight)

    def get_flights_for(self, date):
        return [flight for flight in self.flights if flight.start_time == date]

    def get_flights_before(self, date):
        return [flight for flight in self.flights if flight.start_time < date]

    def get_flights_from(self, city, date):
        if date:
            return [flight for flight in self.flights if flight.from_dest == city and flight.start_time == date]
        return [flight for flight in self.flights if flight.from_dest == city]

    def get_flight_to(self, destination, date):
        if date:
            return [flight for flight in self.flights if flight.to_dest == destination and flight.start_time == date]
        return [flight for flight in self.flights if flight.to_dest == destination]

    def get_terminal_flights(self, terminal, date, to_dest):
        if date:
            return [flight for flight in self.flights if flight.terminal == terminal and flight.start_time == date]
        elif to_dest:
            return [flight for flight in self.flights if flight.terminal == terminal and flight.to_dest == to_dest]
        return [flight for flight in self.flights if flight.terminal == terminal]

    def get_flights_within_duration(self, flight):
        maximum_duration = flight.get_flight_duration()
        return [flight for flight in self.flights if flight.get_flight_duration() <= maximum_duration]

    def get_passengers_to_dest(self, destination):
        return [passenger for flight in self.flights if flight.to_dest == destination for passenger in flight.passengers]

    def get_passengers_from_terminal(self, terminal):
        return [passenger for flight in self.flights if flight.terminal == terminal for passenger in flight.passengers]

    def get_reservations_to_destination(self, destination):
        return [reservation for flight in self.flights
                if flight.to_dest == destination for reservation in flight.reservations]

    def get_flight_hours_duration(self, flight):
        flight_duration = flight.get_flight_duration()
        hours = (flight_duration.years * Date.HOURS_IN_A_YEAR
                  + flight_duration.months * Date.HOURS_IN_A_MONTH
                  + flight_duration.days * Date.HOURS_IN_A_DAY
                  + flight_duration.hours
                  + flight_duration.minutes / 60)
        return hours
