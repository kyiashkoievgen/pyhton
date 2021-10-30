class Cell:
    def __init__(self, num_cel):
        self.num_cel = num_cel

    def __add__(self, other):
        return Cell(self.num_cel + other.num_cel)

    def __sub__(self, other):
        result = self.num_cel - other.num_cel
        if result > 0:
            return Cell(result)
        else:
            raise ValueError ("Ошибка в значении")

    def __mul__(self, other):
        return Cell(self.num_cel * other.num_cel)

    def __truediv__(self, other):
        return Cell(self.num_cel // other.num_cel)

    def make_order(self, n):
        row = self.num_cel // n
        res = self.num_cel - row * n
        return row * (n * "*" + "\n") + res * "*"


c = Cell(10)
c2 = Cell(3)
c3 = c - c2
print(c3.make_order(3))
