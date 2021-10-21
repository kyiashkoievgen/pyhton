class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def mass(self, mkw, w):
        mass_road = self._width * self._length * mkw * w / 1000
        print(f"Масса асфальта {mass_road} т")


length = int(input("Длинна дороги "))
width = int(input("Ширина дороги "))
mk = int(input("Масса одного кв метра "))
h = int(input("Толщина асфальта "))
road = Road(length, width)
road.mass(mk, h)

