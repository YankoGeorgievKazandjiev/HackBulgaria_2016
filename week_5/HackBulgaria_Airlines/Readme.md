# HackBulgaria Airlines

Discover the world with HackBulgaria Airlines!

![HackBulgaria Airlines](airplane.png)

We need to collect the needed information, in order HackBulgaria Airlines to start working with customers. All data is for one airport!

So lets start with the basic stuff:


## Flight

Make a `Flight` class which can be initialized by that (all constructor arguments are shown in the example below).

```python
f = Flight(start_time=Date(29, 11, 2016, hour='12:20'), end_time=Date(29, 11, 2016, hour='15:30'), passengers=100, max_passengers=120, from_dest="Sofia", to_dest="London", terminal=Terminal(2, 30), declined=False)
```

Hint: Create class `Date` with date and hour information!

## Terminal

We also need class `Terminal`. Our airport can have more than 1 terminal. Initialize it with:

```python
t = Terminal(number=1, max_flights=20)
```

## Passenger

Our Flights cannot fly without passengers!

```python
p = Passenger(first_name="Rositsa", last_name="Zlateva", flight=Flight(....), age=22)
```

## Reservation

Our customers cannot fly without reservation!

```python
r = Reservation(flight=Flight(..), passenger=Passenger(..), accepted=True)
```

## Now comes the funny part!

HackBulgaria Airlines need a lot of information to work with its customers!

Your task is to implement not only the basic classes, but a lot of methods, which the Airline needs. It's time for Test-Driven-Development. First tests, then the main implementation!

You are free to add other methods and attributes!

### Flights for date

Implement a method, which returns the flights for a date:

```python
def get_flights_for(date):
    pass
```

### Flight before 'hour'

Implement a method, which returns the flights before 'hour':

```python
def get_flight_before(date, hour):
    pass
```

### Flight from destination

Implement a method, which returns the flights from a destination:

```python
def get_flight_from(destination):
    pass
```

### Flight to destination

Implement a method, which returns the flights to a destination:

```python
def get_flight_to(destination):
    pass
```

### Flight to/from destination at date and hour

Implement a method, which returns the flights from a destination at date and hour:

```python
def get_flight_to(destination, date, hour):
    pass

def get_flight_from(destination, date, hour):
    pass
```

### All flights from terminal

Implement a method, which returns the flights from a terminal:

```python
def get_terminal_flights():
    pass
```

### Flights from terminal on date

Implement a method, which returns the flights from a terminal:

```python
def get_terminal_flights_on(date):
    pass
```

### Flight duration

Implement a method, which returns the flight duration.

```python
def flight_duration():
    pass
```

### All flights to destination from terminal

Method, which returns all flights for a destination from a terminal

```python
def terminal_flights_to_dest(destination):
    pass
```

### All flights with duration less than 'hours' on a 'date'

```python
def flights_on_date_lt_hours(date, hours):
    pass
```

### All flights within duration

```python
def flights_within_duration(start_time, end_time):
    pass
```

### Passengers under 18 for flight

```python
def passengers_under_18(flight):
    pass
```

### Passengers to destination

Method, which returns all passengers from all flights to destination

```python
def passengers_to_dest(destination):
    pass
```

### Passengers from terminal

Method, which returns all passengers flying from terminal

```python
def passengers_from_terminal(terminal):
    pass
```

### Flights with passengers more than 'number'

Implement a method, which returns the flights with passengers greater than a number

```python
def flights_with_passengers(size):
    pass
```

### Passengers reservations for a flight

Implement a method, which returns the reservations of all passengers for flight

```python
def passengers_reservations(flight):
    pass
```

### Reservations to destination

Implement a method, which returns the reservations to destination

```python
def reservations_to_destination(destination):
    pass
```

### Flight has empty seats

Implement a method, which returns if there are empty seats in a flight.

```python
def flight_empty_seats():
    pass
```

#### Think what will happen if a flight is declined??? What will happen with the passengers?
