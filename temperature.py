class Temperature:
    def __init__(self, year, month, day, temp, location):
        self.year = year
        self.month = month
        self.day = day
        self.temp = temp
        self.location = location

    def get_year(self):
        return self.year

    def get_month(self):
        return self.month

    def get_day(self):
        return self.day

    def get_temp(self):
        return self.temp

    def get_location(self):
        return self.location