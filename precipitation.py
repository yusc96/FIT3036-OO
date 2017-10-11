class Precipitation:
    def __init__(self, year, month, day, amount, location):
        self.year = year
        self.month = month
        self.day = day
        self.amount = amount
        self.location = location

    def get_year(self):
        return self.year

    def get_month(self):
        return self.month

    def get_day(self):
        return self.day

    def get_amount(self):
        return self.amount

    def get_location(self):
        return self.location