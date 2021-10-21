class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print("машина поехала")

    def stop(self):
        print("машина остановилась")

    def turn(self, direction):
        print("машина повернула", direction)

    def show_speed(self):
        print(self.speed)


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            print("привышение скорости")


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            print("привышение скорости")


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


car = TownCar(70, "red", "BMW", 0)
print(car.speed, car.name, car.color, car.is_police)
car.go()
car.stop()
car.turn("вправо")
car.show_speed()

car = SportCar(70, "blue", "lada", 0)
print(car.speed, car.name, car.color, car.is_police)
car.go()
car.stop()
car.turn("вправо")
car.show_speed()

car = WorkCar(70, "black", "mers", 0)
print(car.speed, car.name, car.color, car.is_police)
car.go()
car.stop()
car.turn("вправо")
car.show_speed()

car = PoliceCar(70, "black", "mers", 1)
print(car.speed, car.name, car.color, car.is_police)
car.go()
car.stop()
car.turn("вправо")
car.show_speed()