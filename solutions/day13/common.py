from re import match
from decimal import Decimal, getcontext

class Problem:
    def __init__(self, problem_data, offset = 0):
        self.button_a = tuple(map(int, match('^.*\\+([0-9]+),.*\\+([0-9]+)$' ,problem_data[0].split(':')[1]).groups()))
        self.button_b = tuple(map(int, match('^.*\\+([0-9]+),.*\\+([0-9]+)$' ,problem_data[1].split(':')[1]).groups()))
        self.prize = tuple(map(int, match('^.*=([0-9]+),.*=([0-9]+)$' ,problem_data[2].split(':')[1]).groups()))
        if offset:
            self.prize = (self.prize[0] + offset, self.prize[1] + offset)
        x = Decimal(self.prize[0])
        y = Decimal(self.prize[1])
        x1 = Decimal(self.button_a[0])
        y1 = Decimal(self.button_a[1])
        x2 = Decimal(self.button_b[0])
        y2 = Decimal(self.button_b[1])
        xy1x1 = x * y1 / x1
        x2y1x1 = x2 * y1 / x1
        self.m = round((y - xy1x1) / (y2 - x2y1x1), 0)
        self.n = round((x / x1) - (((y - xy1x1) / (y2 - x2y1x1) * x2) / x1), 0)
        self.cost = 0
        if (x1 * self.n) + (x2 * self.m) == x and (y1 * self.n) + (y2 * self.m) == y:
            if offset > 0 or (self.m <= 100 and self.n <= 100):
                self.cost = int(self.m + (3 * self.n))