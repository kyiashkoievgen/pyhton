class Complex:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return Complex(self.a+other.a, self.b+other.b)

    def __mul__(self, other):
        return Complex(self.a*other.a-self.b*other.b, self.a*other.b+self.b*other.a)

    def __str__(self):
        return f"{self.a} j{self.b} "


comp_1 = Complex(2, 5)
comp_2 = Complex(3, 6)
print(comp_1+comp_2)
print(comp_1*comp_2)
