class ZeroDev(Exception):
    def __init__(self, txt):
        self.txt = txt


try:
    a = int(input("введите делимое число="))
    b = int(input("введите делитель="))
    if b == 0:
        raise ZeroDev("делить на ноль нельзя!!!")
except ValueError:
    print("вы ввели не число")
except ZeroDev as err:
    print(err)
else:
    print(a/b)
