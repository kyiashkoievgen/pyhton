class Store:
    def __init__(self, name):
        self.office_equip_list = list()
        self.name = name

    def add_equip(self, eq):
        self.office_equip_list.append(eq)

    def transfer_equip(self, eq, to_store):
        to_store.add_equip(self.office_equip_list[eq])
        self.office_equip_list.pop(eq)

    def print_store_equip(self):
        for el in self.office_equip_list:
            print("на складе", self.name, " содержиться:", el.__class__.__name__, "в количестве:", el.num, "шт весом",
                  el.weight, "производитель:", el.brand)


class OfficeEquipment:
    def __init__(self, weight, num, brand):
        self.weight = weight
        self.num = OfficeEquipment.num_valid(num)
        self.brand = brand

    def get_num_equip(self):
        return self.num

    @staticmethod
    def num_valid(num):
        try:
            return int(num)
        except ValueError:
            print("Количесто должно быть число!")


class Printer(OfficeEquipment):
    def __init__(self, weight, num, brand, pr_type):
        super().__init__(weight, num, brand)
        self.pr_type = pr_type


class Scanner(OfficeEquipment):
    def __init__(self, weight, num, brand, scan_speed):
        super().__init__(weight, num, brand)
        self.scan_speed = scan_speed


class Copier(OfficeEquipment):
    def __init__(self, weight, num, brand, format_paper):
        super().__init__(weight, num, brand)
        self.format_paper = format_paper


copier = Copier(5, 333, "Xerox", "a3")
copier2 = Copier(6, 6, "Canon", "A4")
printer = Printer(2, 10, "Epson", "Laser")
scanner = Scanner(3, 5, "Brother", 102)
store = Store("Основной")
store.add_equip(copier)
store.add_equip(copier2)
store.add_equip(printer)
store.add_equip(scanner)
store2 = Store("Регион 1")
store.transfer_equip(1, store2)
store.print_store_equip()
store2.print_store_equip()
