class OnlyNumber(Exception):

    def __init__(self, txt):
        self.txt = txt

    @staticmethod
    def is_num(data):
        try:
            res = int(data)
        except ValueError:
            print("Вы ввели не число")
        else:
            return res


my_list = list()
while 1:
    d = input("введите число:")
    if d != "stop":
        n = OnlyNumber.is_num(d)
        if n is not None:
            my_list.append(n)
    else:
        print(my_list)
        break
