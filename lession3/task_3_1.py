def my_dev(arg1, arg2):
    if arg2 == 0:
        print("Деление на ноль")
        return
    return arg1 / arg2


n1 = int(input("первый аргумент="))
n2 = int(input("второй аргумент="))
print(my_dev(n1, n2))
