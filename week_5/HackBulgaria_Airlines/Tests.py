from airlines import Airline
from Duration import Duration
from Passenger import Passenger
from Terminal import Terminal
from Reservation import Reservation
from flight_company import Flight
from date_class import Date
import unittest

class AirlineTests(unittest.TestCase):
    def setUp(self):
        # Terminals for flights
        self.terminal_1 = Terminal(1, 20)
        self.terminal_2 = Terminal(2, 30)

        # Sample flights
        self.f = Flight(start_time=Date(29, 11, 2016, hour='13:20'), end_time=Date(29, 11, 2016, hour='15:30'),
                   max_passengers=90, from_dest="Sofia", to_dest="London", terminal=self.terminal_2,
                   declined=False)

        self.f2 = Flight(start_time=Date(29, 10, 2016, hour='10:20'), end_time=Date(30, 11, 2016, hour='23:00'),
                   max_passengers=100, from_dest="London", to_dest="Sofia", terminal=self.terminal_2,
                   declined=False)

        self.f3 = Flight(start_time=Date(30, 11, 2016, hour='14:50'), end_time=Date(30, 11, 2016, hour='18:15'),
                   max_passengers=110, from_dest="Madrid", to_dest="Barcelona", terminal=self.terminal_2,
                   declined=False)

        self.f4 = Flight(start_time=Date(31, 11, 2016, hour='20:20'), end_time=Date(1, 12, 2016, hour='21:21'),
                   max_passengers=150, from_dest="Burgas", to_dest="Paris", terminal=self.terminal_2,
                   declined=False)

        # LONDON
        self.london_passengers = [Passenger('Foo', 'Bar', self.f, 17), Passenger('Bar', 'Foo', self.f, 19)]
        self.london_reservations = [Reservation(self.f, self.london_passengers[0], True),
                               Reservation(self.f, self.london_passengers[1], True)]
        self.f.add_passengers(self.london_passengers)
        self.f.add_reservations(self.london_reservations)
        # SOFIA
        self.sofia_passengers = [Passenger('Foo', 'Bar', self.f2, 21), Passenger('Bar', 'Foo', self.f2, 19)]
        self.sofia_reservations = [Reservation(self.f2, self.sofia_passengers[0], True),
                              Reservation(self.f2, self.sofia_passengers[1], True)]
        self.f2.add_passengers(self.sofia_passengers)
        self.f2.add_reservations(self.sofia_reservations)
        # BARCELONA
        self.barcelona_passengers = [Passenger('Lo', 'Dash', flight=self.f3, age=34),
                                Passenger('Dash', 'Lo', flight=self.f3, age=40)]
        self.barcelona_reservations = [Reservation(self.f3, self.barcelona_passengers[0], True),
                                  Reservation(self.f3, self.barcelona_passengers[1], True)]
        self.f3.add_passengers(self.barcelona_passengers)
        self.f3.add_reservations(self.barcelona_reservations)

        # Our Airline class holding our flights
        self.airline_dummy = Airline(flights=[self.f, self.f2, self.f3, self.f4])

    def test_airline_class_constructor(self):
        self.assertTrue(isinstance(self.airline_dummy, Airline))
        self.assertEqual(len(self.airline_dummy.flights), 4)
        self.assertEqual(self.airline_dummy.flights[-1].to_dest, "Paris")

    def test_airline_get_flights_for(self):
        self.assertEqual(self.airline_dummy.get_flights_for(Date(29, 11, 2016, '00:00')), [self.f])
        self.assertEqual(self.airline_dummy.get_flights_for(Date(29, 4314, 2016, '00:00')), [])

    def test_airline_get_flights_before(self):
        self.assertEqual(self.airline_dummy.get_flights_before(Date(29, 11, 2016, '23:59')), [self.f, self.f2])
        self.assertEqual(self.airline_dummy.get_flights_before(Date(29, 11, 24141, '23:59')),
                         [self.f, self.f2, self.f3, self.f4])

    def test_airline_get_flights_from(self):
        self.assertEqual(
            self.airline_dummy.get_flights_from(city = 'Burgas', date = self.f4.start_time),
            [self.f4]
        )
        self.assertEqual(
            self.airline_dummy.get_flights_from(city = 'Burgas', date = self.f3.start_time),
            []
        )

    def test_airline_get_flights_to_with_date(self):
        # with dates
        self.assertEqual(
            self.airline_dummy.get_flight_to(destination='Paris', date=self.f4.start_time),
            [self.f4]
        )
        self.assertEqual(
            self.airline_dummy.get_flight_to(destination='Paris', date=self.f3.start_time),
            []
        )

    def test_airline_get_terminal_flights(self):
        """ Get all the flights that are flying from a specific terminal """
        terminal_3 = Terminal(number=3, max_flights=20)

        # all our dummy flights come from terminal 2
        self.assertEqual(
            self.airline_dummy.get_terminal_flights(terminal=self.terminal_2),
            [self.f, self.f2, self.f3, self.f4]
        )
        self.assertEqual(
            self.airline_dummy.get_terminal_flights(terminal=terminal_3),
            []
        )

    def test_airline_get_terminal_flights_on(self):
        """ Get all the flights that are flying from a specific terminal on a given date"""
        terminal_3 = Terminal(number=3, max_flights=20)
        self.assertEqual(
            self.airline_dummy.get_terminal_flights(terminal=self.terminal_2, date=self.f2.start_time),
            [self.f2]
        )
        self.assertEqual(
            self.airline_dummy.get_terminal_flights(terminal=terminal_3, date=Date(0, 0, 0000, '00:00')),
            []
        )

    def test_airline_terminal_flights_to_dest(self):
        """ Get all the flights that are flying from a specific terminal and headed to the given city"""
        test_destination = 'Barcelona'
        self.assertEqual(self.airline_dummy.get_terminal_flights(terminal=self.terminal_2, to_dest=test_destination),
                         [self.f3])

        self.assertEqual(self.airline_dummy.get_terminal_flights(terminal=self.terminal_1, to_dest=test_destination),
                         [])


    def test_airline_flights_within_duration(self):
        """ Get the flights whose durations are within the duration of another flight"""
        self.assertEqual(self.airline_dummy.get_flights_within_duration(self.f2),
                         [self.f, self.f2 ,self.f3, self.f4])
        self.assertEqual(self.airline_dummy.get_flights_within_duration(self.f),
                         [self.f])

    def test_airline_get_passengers_to_dest(self):
        """ Get all the passengers who are flying to a destination"""
        self.assertEqual(len(self.airline_dummy.get_passengers_to_dest('Barcelona')), 2)
        self.assertEqual(len(self.airline_dummy.get_passengers_to_dest('NOWHERE')), 0)

        paris_passengers = [Passenger('Mu', 'Ku', flight=self.f4, age=30),
                            Passenger('MuS', 'KuS', flight=self.f4, age=30)]
        paris_reservations = [Reservation(flight=self.f4, passenger=paris_passengers[0], accepted=True),
                              Reservation(flight=self.f4, passenger=paris_passengers[1], accepted=True)]
        self.f4.add_passengers(paris_passengers)
        self.f4.add_reservations(paris_reservations)

        self.assertEqual(self.airline_dummy.get_passengers_to_dest('Paris'), paris_passengers)

    def test_airline_get_passengers_from_terminal(self):
        """ Get all the passengers that are flying from a terminal"""
        self.assertEqual(len(self.airline_dummy.get_passengers_from_terminal(self.terminal_2)), 6)
        self.assertEqual(len(self.airline_dummy.get_passengers_from_terminal(self.terminal_1)), 0)

    def test_airline_get_reservations_to_destination(self):
        """ Get all the reservations that are to a specific destination """
        self.assertEqual(self.airline_dummy.get_reservations_to_destination('London'), self.london_reservations)
        self.assertEqual(self.airline_dummy.get_reservations_to_destination('NOWHERE'), [])



if __name__ == '__main__':
    unittest.main()
