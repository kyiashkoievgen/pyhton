class Worker:
    _income = {"wage": 13000, "bonus": 500}

    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position


class Position(Worker):
    def __init__(self, name, surname, position):
        super().__init__(name, surname, position)

    def get_full_name(self):
        return self.name + " " + self.surname

    def get_total_income(self):
        return self._income["wage"] + self._income["bonus"]


pos = Position("ewgen", "kyiashko", "chief")
print(pos.get_full_name())
print(pos.get_total_income())
print(pos.position)
