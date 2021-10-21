class Stationery:
    title = "Канцелярия"

    def draw(self):
        print("запуск отрисовки")


class Pen(Stationery):
    def draw(self):
        print("запуск ручки")


class Pencil(Stationery):
    def draw(self):
        print("запуск карандаша")


class Handle(Stationery):
    def draw(self):
        print("запуск маркера")


stationery = Stationery()
stationery.draw()
pen = Pen()
pen.draw()
pencil = Pencil()
pencil.draw()
handle = Handle()
handle.draw()
