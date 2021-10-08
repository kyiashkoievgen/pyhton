
def my_func(x, y):
    x = abs(x)
    y = abs(round(y))
    result = x
    for i in range(1, y):
        result = result * x
    return 1 / result


input_x = int(input("Введите действительное положительное число x:"))
input_y = int(input("Введите целое отрицательное число y:"))
print("x^y=", my_func(input_x, input_y))
