class Duration:
    def __init__(self, years, months, days, hours, minutes):
        self.years = years
        self.months = months
        self.days = days
        self.hours = hours
        self.minutes = minutes

    def __eq__(self, other):
        return (self.years == other.years and self.months == other.months and
                self.days == other.days and self.hours == other.hours and
                self.minutes == other.minutes)

    def __gt__(self, other):
        return (self.years > other.years and self.months > other.months and
                self.days > other.days and self.hours > other.hours and
                self.minutes > other.minutes)

    def __lt__(self, other):
        return not self.__gt__(other)

    def __ge__(self, other):
        return self.__gt__(other) or self.__eq__(other)

    def __le__(self, other):
        return self.__lt__(other) or self.__eq__(other)
