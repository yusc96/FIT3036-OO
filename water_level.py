class Water_level:
    def __init__(self, year, month, day, amount):
        self.year = year
        self.month = month
        self.day = day
        self.amount = amount

    def get_year(self):
        return self.year

    def get_month(self):
        return self.month

    def get_day(self):
        return self.day

    def get_amount(self):
        return self.amount