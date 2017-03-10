from Duration import Duration


class Date:

    HOURS_IN_A_YEAR = 8765.81277
    HOURS_IN_A_MONTH = 730.484398
    HOURS_IN_A_DAY = 24

    def __init__(self, day, month, year, hour):
        self.day = day
        self.month = month
        self.year = year
        self.hour = hour

    def __eq__(self, other):
        return (self.day == other.day and
                self.month == other.month and
                self.year == other.year)

    def __gt__(self, other):
        if self.year > other.year:
            return True
        elif self.year == other.year:
            if self.month > other.month:
                return True
            elif self.month == other.month:
                if self.day > other.day:
                    return True
                elif self.day == other.day:
                    if self.hour > other.hour:
                        return True
        return False

    def __lt__(self, other):
        return not self.__gt__(other)

    def __ge__(self, other):
        return (self.year > other.year) or (self.month > other.month) or (self.day > other.day) or (self.hour >= self.hour)

    def __le__(self, other):
        return (self.year < other.year) or (self.month < other.month) or (self.day < other.day) or (self.hour <= self.hour)

    def __sub__(self, other):
        hours, minutes = tuple([int(x) for x in self.hour.split(':')])
        other_hours, other_minutes = tuple([int(x) for x in other.hour.split(':')])

        minute_difference = minutes-other_minutes
        if minute_difference < 0:
            hours -= 1
            minute_difference = 60 - abs(minute_difference)

        hour_difference = hours-other_hours
        day = self.day
        if hour_difference < 0:
            day -= 1
            hour_difference = 24 - abs(hour_difference)

        day_difference = day - other.day
        month = self.month
        if day_difference < 0:
            month -= 1
            day_difference = 31 - abs(day_difference)

        month_difference = month - other.month
        year = self.year
        if month_difference < 0:
            year -= 1
            month_difference = 12 - abs(month_difference)

        year_difference = year - other.year

        return Duration(years = year_difference, months = month_difference,
                        days = day_difference, hours = hour_difference, minutes = minute_difference)
